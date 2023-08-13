"""Data reading and processing module."""
import logging
import warnings

import pandas as pd
from omegaconf import DictConfig
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)


def prepare_data(cfg: DictConfig) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Read and prepare data for model training.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.

    Returns
    -------
    X_train : pd.DataFrame
        Data with feature variables for training.
    X_test : pd.DataFrame
        Data with target variable for testing.
    y_train : pd.Series
        Data with feature variables for training.
    y_test : pd.Series
        Data with target variable for testing.
    """
    # Load the diabetes dataset
    data = pd.read_csv(cfg.data.file_path)

    # Check data
    _check_data(data)

    # Get X and y column names
    X_colnames = cfg.data.x_colnames
    y_colname = cfg.data.y_colname

    # Split into X and y
    X = data.loc[:, X_colnames]
    y = data.loc[:, y_colname]

    # Split into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test


def _check_data(data: pd.DataFrame) -> None:
    """Check if data fit certain properties, and raise warnings/errors if not.

    For internal use.

    Parameters
    ----------
    data : pd.DataFrame
        Data to be checked.

    Returns
    -------
    None
    """
    if not data.empty:
        if not all(data.dtypes == float):
            if any(data.dtypes == object):
                logger.exception("Data contains string or mixed type. Please handle the data manually.")
                raise Exception("Data contains string or mixed type. Please handle the data manually.")
            elif any(data.dtypes == int):
                logger.warning("Data contains integer. Please check if this is intended.")
                warnings.warn("Data contains integer. Please check if this is intended.")
        else:
            logger.info("All data checks passed!")
    else:
        logger.exception("Empty dataframe. Please check the data.")
        raise Exception("Empty dataframe. Please check the data.")
