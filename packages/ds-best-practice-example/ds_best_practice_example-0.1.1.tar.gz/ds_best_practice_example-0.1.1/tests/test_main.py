"""Tests for ezml.main.

Contains tests on command line outputs.
"""
import os
import subprocess
from contextlib import contextmanager

# (A) Helper functions


@contextmanager
def inside_dir(dirpath: str) -> None:
    """Execute code from inside the given directory.

    Parameters
    ----------
    dirpath : str
        Path of the directory the command is being run.

    Returns
    -------
    None
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def execute(command: list[str], dirpath: str, timeout: int = 30, supress_warning: bool = True) -> str:
    """Run command inside given directory and returns output.

    If there's stderr, then it may raise exception according to supress_warning.

    Parameters
    ----------
    command : list[str]
        List of commands to be run.
        E.g. ["python main.py --help"]
    dirpath : str
        Path of the directory the command is being run.
    timeout : int
        Seconds to command timeout.
    supress_warning : bool
        Whether to suppress warning.

    Returns
    -------
    out : str
        Output from standard out.
    """
    with inside_dir(dirpath):
        proc = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    out, err = proc.communicate(timeout=timeout)
    out = out.decode("utf-8")
    err = err.decode("utf-8")

    if err and not supress_warning:
        raise RuntimeError(err)
    else:
        print(err)
        return out


# (B) Tests


def test_cli_help() -> None:
    """Test the command line interface (CLI) help interface."""
    cli_path = "./"

    cli_out = execute(["ezml", "--help"], str(cli_path))
    assert "Powered by Hydra (https://hydra.cc)" in cli_out
    assert "Use --hydra-help to view Hydra specific help" in cli_out


def test_cli_default() -> None:
    """Test the command line interface (CLI) default run."""
    cli_path = "./"

    cli_out = execute(["ezml"], str(cli_path))
    assert "Mean squared error" in cli_out
    assert "Coefficient of determination" in cli_out
    assert "Pipeline ended - Linear regression." in cli_out
