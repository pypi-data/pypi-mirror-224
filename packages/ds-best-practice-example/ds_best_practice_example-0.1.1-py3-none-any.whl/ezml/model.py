"""Model training and inference module."""
import logging

import joblib
import pandas as pd
from omegaconf import DictConfig
from sklearn import linear_model

logger = logging.getLogger(__name__)


def train_model(cfg: DictConfig, X_train: pd.DataFrame, y_train: pd.Series) -> linear_model.LinearRegression:
    """Train a linear regression on data, and save the trained model.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.
    X_train : pd.DataFrame
        Data with feature variables for training.
    y_train : pd.Series
        Data with target variable for training.

    Returns
    -------
    model : linear_model.LinearRegression
        Trained linear regression model.
    """
    # Create linear regression object
    model = linear_model.LinearRegression()

    # Train the model using the training sets
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, cfg.model.file_path)

    return model
