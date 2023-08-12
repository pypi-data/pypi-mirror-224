import re
from datetime import timedelta
from typing import Dict

import pandas as pd
from loguru import logger as logging

from ngcpp.cluster import Cluster
from ngcpp.utils import parse_duration, run_simple_command

# pylint: disable=W0640, W1401


def resume_jobs_cluster(
    job_resume_cmd: Dict[str, str],
    alias="10",
):
    cluster = Cluster(alias)

    jobs_all_df = cluster.jobs()
    jobs_all_df["Duration"] = jobs_all_df["Duration"].apply(parse_duration)
    for job_name, cmd in job_resume_cmd.items():
        # job name must follow the format: job_name or job_name + _ngcpp_resubmit_ + resubmit_number
        # Define a function to check if the name matches the desired pattern
        def filter_job_name(name):
            return name == job_name or bool(  # pylint: disable=W0640
                re.match(f"{job_name}_ngcpp_resubmit_\d+", name)
            )

        # Use the function to filter the DataFrame
        cur_jobs_df = jobs_all_df[jobs_all_df["Name"].apply(filter_job_name)]

        # Extract the resubmit_number from the 'Name' column
        def extract_resubmit_number(name):
            match = re.search(
                f"{job_name}_ngcpp_resubmit_(\d+)", name  # pylint: disable=W0640
            )
            return int(match.group(1)) if match else 0

        cur_jobs_df["resubmit_number"] = cur_jobs_df["Name"].apply(
            extract_resubmit_number
        )

        # Sort the cur_jobs_df by resubmit_number, largest first
        cur_jobs_df = cur_jobs_df.sort_values(by="resubmit_number", ascending=False)

        latest_job_row = cur_jobs_df.iloc[0]

        if is_resubmit_job(latest_job_row, cluster):
            resubmit_number = latest_job_row["resubmit_number"] + 1
            cmd = cmd.replace(job_name, f"{job_name}_ngcpp_resubmit_{resubmit_number}")
            logging.info(f"Resubmitting job {job_name} \n {cmd}")
            run_simple_command(f"ngc batch kill {latest_job_row['Id']}")
            stdout, stderr = run_simple_command(cmd)
            logging.trace(f"\n \t stdout: {stdout}")
            if stderr:
                logging.info(f"\n \t stderr: {stderr}")


def is_resubmit_job(job_row: pd.Series, cluster: Cluster):
    """
    * If the job is in QUEUED / STARTING / FAILED, return false
    * If the job in RUNNING, if duration is less than Duration less than 1h, return false
    * If the job in RUNNING, if duration is less than Duration greater than 1h, check hang time
    """
    # Check for QUEUED, STARTING, or FAILED status
    if job_row["Status"] in ["QUEUED", "STARTING", "KILLED_BY_USER"]:
        logging.debug(f"Job {job_row['Id']} is in {job_row['Status']} status, skip")
        return False
    if job_row["Status"] == "RUNNING" and job_row["Duration"] < 1:
        # Check for RUNNING status with duration less than 1 hour
        logging.debug(
            f"Job {job_row['Id']} is in {job_row['Status']} status and less than 1h, skip"
        )
        return False
    if job_row["Status"] in ["FAILED", "KILLED_BY_SYSTEM"]:
        logging.info(f"Job {job_row['Id']} is in {job_row['Status']} status, resubmit")
        return True
    if job_row["Status"] == "RUNNING" and job_row["Duration"] >= 1:
        hang_time, _ = cluster.check_one_job_hang(job_row["Id"])
        if hang_time > timedelta(hours=1):
            logging.info(
                f"Job {job_row['Id']} is in {job_row['Status']} status and hang for more than 1h, resubmit"
            )
            return True
        logging.info(
            f"Job {job_row['Id']} is in {job_row['Status']} status and hang for less than 1h, skip"
        )
        return False

    raise NotImplementedError(f"Unexpected job status: {job_row['Status']}")
