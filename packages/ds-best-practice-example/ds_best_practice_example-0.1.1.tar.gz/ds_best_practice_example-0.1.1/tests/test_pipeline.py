"""Tests for ezml.pipeline."""
import logging

import hydra
import pytest

from ezml.pipeline import linear_regression_pipeline


def test_linear_regression_pipeline(caplog: pytest.LogCaptureFixture) -> None:
    """Test the linear_regression_pipeline function.

    Parameters
    ----------
    caplog : pytest.LogCaptureFixture
        Pytest captured logging output.

    Returns
    -------
    None
    """
    # Set logging at lowest level to capture everything
    with hydra.initialize(version_base=None, config_path="../input/conf"), caplog.at_level(logging.DEBUG):
        cfg = hydra.compose(config_name="config")

        linear_regression_pipeline(cfg=cfg)

    assert "Component ended - Data preparation." in caplog.text
    assert "Component ended - Model training." in caplog.text
    assert "Component ended - Model diagnosis." in caplog.text
