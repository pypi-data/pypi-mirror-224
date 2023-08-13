"""Tests for ezml.model.

Contains tests on trained model outputs & computation time.
"""
import math
import pathlib

import hydra
import pandas as pd
import pytest
from sklearn.metrics import mean_squared_error, r2_score

from ezml.model import train_model


@pytest.mark.parametrize(
    "X_train, y_train, mse_exp, r2_exp",
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
            0.0,
            1.0,
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
            0.667,
            0.0,
        ),
    ],
)
@pytest.mark.timeout(10)
def test_train_model_results(X_train: pd.DataFrame, y_train: pd.Series, mse_exp: float, r2_exp: float) -> None:
    """Test the train_model function, with known expected results.

    Each computation must complete within 10 seconds.

    Parameters
    ----------
    X_train : pd.DataFrame
        Data with feature variables for training.
    y_train : pd.Series
        Data with target variable for training.
    mse_exp : float
        Expected MSE score.
    r2_exp : float
        Expected R2 score.

    Returns
    -------
    None
    """
    with hydra.initialize(version_base=None, config_path="../input/conf"):
        cfg = hydra.compose(config_name="config", overrides=["model.file_path=./output/model/linreg_diabetes.joblib"])

        model = train_model(cfg, X_train, y_train)

        # Make predictions using the testing set
        y_pred = model.predict(X_train)

        # Report model performance
        mse_res = mean_squared_error(y_train, y_pred)
        r2_res = r2_score(y_train, y_pred)

        assert math.isclose(mse_res, mse_exp, abs_tol=0.001)
        assert math.isclose(r2_res, r2_exp, abs_tol=0.001)


@pytest.mark.parametrize(
    "X_train, y_train",
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
        ),
    ],
)
@pytest.mark.timeout(10)
def test_train_model_file_output(X_train: pd.DataFrame, y_train: pd.Series, tmp_path: pathlib.Path) -> None:
    """Test the train_model function, to check if model is exported.

    Each computation must complete within 10 seconds.

    Parameters
    ----------
    X_train : pd.DataFrame
        Data with feature variables for training.
    y_train : pd.Series
        Data with target variable for training.
    tmp_path : pathlib.Path
        Pytest temporary folder for this unit test.

    Returns
    -------
    None
    """
    with hydra.initialize(version_base=None, config_path="../input/conf"):
        out_path = tmp_path / "linreg_diabetes.joblib"

        cfg = hydra.compose(config_name="config", overrides=[f"model.file_path={out_path}"])

        _ = train_model(cfg, X_train, y_train)

        assert out_path.exists()
