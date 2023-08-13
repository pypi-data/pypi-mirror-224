"""Tests for ezml.diagnostic.

Contains tests on synthetic data frame.
"""
import logging

import pandas as pd
import pytest
from sklearn import linear_model

from ezml.diagnostic import diagnose_model


@pytest.mark.parametrize(
    "X_train, y_train, X_test, y_test, mse_exp, r2_exp",
    [
        (
            pd.DataFrame(
                {
                    "featA": [1.0, 0.0, 0.0],
                    "featB": [0.0, 1.0, 0.0],
                    "featC": [0.0, 0.0, 1.0],
                }
            ),
            pd.Series([1.0, 2.0, 3.0], name="target"),
            pd.DataFrame(
                {
                    "featA": [0.5, 0.0, 0.0],
                    "featB": [1.0, 0.0, 0.0],
                    "featC": [0.5, 1.0, 0.0],
                }
            ),
            pd.Series([0.5, 1.0, 2.5], name="target"),
            2.167,
            -2.0,
        ),
        (
            pd.DataFrame(
                {
                    "featA": [0.0, 0.0, 0.0],
                    "featB": [0.0, 0.0, 0.0],
                    "featC": [0.0, 0.0, 0.0],
                }
            ),
            pd.Series([1.0, 2.0, 3.0], name="target"),
            pd.DataFrame(
                {
                    "featA": [0.0, 0.0, 0.0],
                    "featB": [0.0, 0.0, 0.0],
                    "featC": [0.0, 0.0, 0.0],
                }
            ),
            pd.Series([0.5, 1.0, 2.5], name="target"),
            1.167,
            -0.615,
        ),
    ],
)
def test_diagnose_model_metrics(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    mse_exp: float,
    r2_exp: float,
    caplog: pytest.LogCaptureFixture,
):
    """Test the diagnose_model function, with known expected results.

    Parameters
    ----------
    X_train : pd.DataFrame
        Data with feature variables for training.
    y_train : pd.Series
        Data with target variable for training.
    X_test : pd.DataFrame
        Data with feature variables for testing.
    y_test : pd.Series
        Data with target variable for testing.
    mse_exp : float
        Expected MSE score.
    r2_exp : float
        Expected R2 score.
    caplog : pytest.LogCaptureFixture
        Pytest captured logging output.

    Returns
    -------
    None
    """
    # Create linear regression object
    model = linear_model.LinearRegression()

    # Train the model using the training sets
    model.fit(X_train, y_train)

    # Set logging at lowest level to capture everything
    with caplog.at_level(logging.DEBUG):
        diagnose_model(X_test, y_test, model)

    assert f"Mean squared error: {mse_exp:.3f}" in caplog.text
    assert f"Coefficient of determination: {r2_exp:.3f}" in caplog.text
