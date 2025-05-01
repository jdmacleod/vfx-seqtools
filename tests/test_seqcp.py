"""Tests for the vfx-seqtools seqcp CLI utility."""

import builtins
import logging
import shutil

import pytest
from pytest_mock import MockFixture
from typer.testing import CliRunner

from vfx_seqtools.seqcp_cli import app

runner = CliRunner(mix_stderr=False)


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


def test_seqcp_calls_shutil_copy2(mocker: MockFixture) -> None:
    """Test that the seqcp command calls shutil copy2 to copy a file."""
    mocker.patch("shutil.copy2", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "newfile.@.txt", "-f", "10-10"])
    assert result.exit_code == 0
    shutil.copy2.assert_called_once_with("file.0010.txt", "newfile.10.txt")  # type: ignore[attr-defined]


def test_seqcp_honors_dry_run(mocker: MockFixture) -> None:
    """Test that the seqcp command honors dry-run option."""
    mocker.patch("shutil.copy2", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "-n"])
    assert result.exit_code == 0
    shutil.copy2.assert_not_called()  # type: ignore[attr-defined]


def test_seqcp_honors_verbose_option(
    mocker: MockFixture, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the seqcp command honors verbose option."""
    caplog.set_level(
        logging.INFO, logger="rich"
    )  # Set the rich caplog level to INFO and above
    mocker.patch("shutil.copy2", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "-v"])
    assert result.exit_code == 0
    shutil.copy2.assert_called_once_with("file.0010.txt", "newfile.10.txt")  # type: ignore[attr-defined]
    assert "COPY: file.0010.txt newfile.10.txt" in caplog.text
    caplog.clear()


def test_seqcp_honors_interactive_option_yes(mocker: MockFixture) -> None:
    """Test that the seqcp command honors 'yes' with interactive option."""
    mocker.patch("shutil.copy2", return_value=True)
    mocker.patch("builtins.input", return_value="y")
    result = runner.invoke(
        app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "--interactive"]
    )
    assert result.exit_code == 0
    shutil.copy2.assert_called_once_with("file.0010.txt", "newfile.10.txt")  # type: ignore[attr-defined]
    builtins.input.assert_called_once_with(  # type: ignore[attr-defined]
        "copy file.0010.txt -> newfile.10.txt? (y/n): "
    )  # type: ignore[attr-defined]


def test_seqcp_honors_interactive_option_no(mocker: MockFixture) -> None:
    """Test that the seqcp command honors 'no' with interactive option."""
    mocker.patch("shutil.copy2", return_value=True)
    mocker.patch("builtins.input", return_value="n")
    result = runner.invoke(
        app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "--interactive"]
    )
    assert result.exit_code == 0
    shutil.copy2.assert_not_called()  # type: ignore[attr-defined]
    builtins.input.assert_called_once_with(  # type: ignore[attr-defined]
        "copy file.0010.txt -> newfile.10.txt? (y/n): "
    )  # type: ignore[attr-defined]
