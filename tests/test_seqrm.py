"""Tests for the vfx-seqtools seqrm CLI utility."""

import builtins
import logging
import pathlib

import pytest
from pytest_mock import MockFixture
from typer.testing import CliRunner

from vfx_seqtools.seqrm_cli import app

runner = CliRunner(mix_stderr=False)


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


def test_seqrm_calls_pathlib_unlink(mocker: MockFixture) -> None:
    """Test that the seqrm command calls pathlib to unlink a file."""
    mocker.patch("pathlib.Path.unlink", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "-f", "10-10"])
    assert result.exit_code == 0
    pathlib.Path.unlink.assert_called_once_with(pathlib.Path("file.0010.txt"))  # type: ignore[attr-defined]


def test_seqrm_honors_dry_run(mocker: MockFixture) -> None:
    """Test that the seqrm command honors dry-run option."""
    mocker.patch("pathlib.Path.unlink", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "-f", "10-10", "-n"])
    assert result.exit_code == 0
    pathlib.Path.unlink.assert_not_called()  # type: ignore[attr-defined]


def test_seqrm_honors_verbose_option(
    mocker: MockFixture, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the seqrm command honors verbose option."""
    caplog.set_level(
        logging.INFO, logger="rich"
    )  # Set the rich caplog level to INFO and above
    mocker.patch("pathlib.Path.unlink", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "-f", "10-10", "-v"])
    assert result.exit_code == 0
    pathlib.Path.unlink.assert_called_once_with(pathlib.Path("file.0010.txt"))  # type: ignore[attr-defined]
    assert "DELETE: file.0010.txt" in caplog.text
    caplog.clear()


def test_seqrm_honors_interactive_option_yes(mocker: MockFixture) -> None:
    """Test that the seqrm command honors 'yes' with interactive option."""
    mocker.patch("pathlib.Path.unlink", return_value=True)
    mocker.patch("builtins.input", return_value="y")
    result = runner.invoke(app, ["file.####.txt", "-f", "10-10", "--interactive"])
    assert result.exit_code == 0
    pathlib.Path.unlink.assert_called_once_with(pathlib.Path("file.0010.txt"))  # type: ignore[attr-defined]
    builtins.input.assert_called_once_with("delete file.0010.txt? (y/n): ")  # type: ignore[attr-defined]


def test_seqrm_honors_interactive_option_no(mocker: MockFixture) -> None:
    """Test that the seqrm command honors 'yes' with interactive option."""
    mocker.patch("pathlib.Path.unlink", return_value=True)
    mocker.patch("builtins.input", return_value="n")
    result = runner.invoke(app, ["file.####.txt", "-f", "10-10", "--interactive"])
    assert result.exit_code == 0
    pathlib.Path.unlink.assert_not_called()  # type: ignore[attr-defined]
    builtins.input.assert_called_once_with("delete file.0010.txt? (y/n): ")  # type: ignore[attr-defined]
