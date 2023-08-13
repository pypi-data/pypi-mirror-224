"""Pipeline definitions."""
import logging
import time

from omegaconf import DictConfig

from ezml.data import prepare_data
from ezml.diagnostic import diagnose_model
from ezml.model import train_model

logger = logging.getLogger(__name__)


def linear_regression_pipeline(cfg: DictConfig) -> None:
    """Pipeline to create a linear regression model based on input data.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.

    Returns
    -------
    None
    """
    logger.info("Component started - Data preparation.")
    start_time = time.time()
    X_train, X_test, y_train, y_test = prepare_data(cfg)
    end_time = time.time()
    logger.info(f"Component ended - Data preparation. Time elapsed : {end_time-start_time:.3f} secs.")

    logger.info("Component started - Model training.")
    start_time = time.time()
    model = train_model(cfg, X_train, y_train)
    end_time = time.time()
    logger.info(f"Component ended - Model training. Time elapsed : {end_time-start_time:.3f} secs.")

    logger.info("Component started - Model diagnosis.")
    start_time = time.time()
    diagnose_model(X_test, y_test, model)
    end_time = time.time()
    logger.info(f"Component ended - Model diagnosis. Time elapsed : {end_time-start_time:.3f} secs.")
