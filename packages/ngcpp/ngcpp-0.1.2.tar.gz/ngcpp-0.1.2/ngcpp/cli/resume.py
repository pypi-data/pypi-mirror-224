import os
import sys
import time

import typer
from loguru import logger as logging
from omegaconf import OmegaConf

from ngcpp.cluster import ALIAS_TO_CLUSTER
from ngcpp.jobs import resume_jobs_cluster
from ngcpp.utils import LOG_FORMAT

# app = typer.Typer()

NGCPP_DIR = os.environ.get("NGCPP_DIR", os.path.expanduser("~/.ngcpp"))
os.makedirs(f"{NGCPP_DIR}/logs", exist_ok=True)

logging.remove()
logging.add(
    # f"ngcpp/logs/resume.log",
    f"{NGCPP_DIR}/logs/resume.log",
    format=LOG_FORMAT,
    enqueue=True,
    catch=True,
)
logging.add(sys.stderr, format=LOG_FORMAT, enqueue=True, catch=True)


@typer.run
def resume(
    cfg: str = typer.Argument(
        "ngc_resume.yaml",
        help="define job in yaml file to track",
        show_default=True,
    ),
    every_n_minutes: int = typer.Option(
        31,
        "-m",
        help="polling time for auto-resume~(every n minutes)",
        show_default=True,
    ),
):
    """
    Auto-resume jobs, polling every n minutes, kill jobs that hang when necessary.
    """
    while True:
        cfg = OmegaConf.load(cfg)
        for cluster_alias, jobs in cfg.items():
            logging.info(f"Resuming jobs in {ALIAS_TO_CLUSTER[cluster_alias]}")
            resume_jobs_cluster(jobs, cluster_alias)
        logging.info(f"Sleeping for {every_n_minutes} minutes")
        time.sleep(every_n_minutes * 60)
