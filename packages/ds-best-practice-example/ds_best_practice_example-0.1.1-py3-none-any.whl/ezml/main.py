"""Entrypoint for ezml."""
import logging
import time

import hydra
from omegaconf import DictConfig

from ezml.pipeline import linear_regression_pipeline

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="../input/conf", config_name="config")
def main(cfg: DictConfig) -> None:
    """Main entrypoint.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.

    Returns
    -------
    None
    """
    # Execute pipeline
    logger.info("Pipeline started - Linear regression.")
    start_time = time.time()
    linear_regression_pipeline(cfg=cfg)
    end_time = time.time()
    logger.info(f"Pipeline ended - Linear regression. Time elapsed : {end_time-start_time:.3f} secs.")


if __name__ == "__main__":
    main()  # pragma: no cover
