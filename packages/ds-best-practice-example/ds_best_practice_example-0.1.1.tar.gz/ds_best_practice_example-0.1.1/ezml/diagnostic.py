"""Model diagnostic module."""
import logging

import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

logger = logging.getLogger(__name__)


def diagnose_model(X_test: pd.DataFrame, y_test: pd.DataFrame, model: linear_model.LinearRegression) -> None:
    """Diagnose the trained model to assess performance.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.
    X_test : pd.Series
        Data with target variable for testing.
    y_test : pd.Series
        Data with target variable for testing.
    model : linear_model.LinearRegression
        Trained linear regression model.

    Returns
    -------
    None
    """
    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # Report model performance
    logger.info(f"Mean squared error: {mean_squared_error(y_test, y_pred):.3f}")
    logger.info(f"Coefficient of determination: {r2_score(y_test, y_pred):.3f}")
