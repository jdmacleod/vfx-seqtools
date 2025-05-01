"""Tests for the vfx-seqtools seqmv CLI utility."""

import builtins
import logging
import shutil

import pytest
from pytest_mock import MockFixture
from typer.testing import CliRunner

from vfx_seqtools.seqmv_cli import app

runner = CliRunner(mix_stderr=False)


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


def test_seqmv_calls_shutil_move(mocker: MockFixture) -> None:
    """Test that the seqmv command calls shutil to move a file."""
    mocker.patch("shutil.move", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "newfile.@.txt", "-f", "10-10"])
    assert result.exit_code == 0
    shutil.move.assert_called_once_with("file.0010.txt", "newfile.10.txt")  # type: ignore[attr-defined]


def test_seqmv_honors_dry_run(
    mocker: MockFixture, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the seqmv command honors dry-run option."""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    mocker.patch("shutil.move", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "-n"])
    assert result.exit_code == 0
    shutil.move.assert_not_called()  # type: ignore[attr-defined]
    assert result.stdout == ""
    assert "dry-run: MOVE" in caplog.text
    caplog.clear()


def test_seqmv_honors_verbose_option(
    mocker: MockFixture, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the seqmv command honors verbose option."""
    caplog.set_level(
        logging.INFO, logger="rich"
    )  # Set the rich caplog level to INFO and above
    mocker.patch("shutil.move", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "-v"])
    assert result.exit_code == 0
    shutil.move.assert_called_once_with("file.0010.txt", "newfile.10.txt")  # type: ignore[attr-defined]
    assert "MOVE: file.0010.txt newfile.10.txt" in caplog.text
    caplog.clear()


def test_seqmv_honors_interactive_option_yes(mocker: MockFixture) -> None:
    """Test that the seqmv command honors 'yes' with interactive option."""
    mocker.patch("shutil.move", return_value=True)
    mocker.patch("builtins.input", return_value="y")
    result = runner.invoke(
        app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "--interactive"]
    )
    assert result.exit_code == 0
    shutil.move.assert_called_once_with("file.0010.txt", "newfile.10.txt")  # type: ignore[attr-defined]
    builtins.input.assert_called_once_with(  # type: ignore[attr-defined]
        "move file.0010.txt -> newfile.10.txt? (y/n): "
    )  # type: ignore[attr-defined]


def test_seqmv_honors_interactive_option_no(mocker: MockFixture) -> None:
    """Test that the seqmv command honors 'no' with interactive option."""
    mocker.patch("shutil.move", return_value=True)
    mocker.patch("builtins.input", return_value="n")
    result = runner.invoke(
        app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "--interactive"]
    )
    assert result.exit_code == 0
    shutil.move.assert_not_called()  # type: ignore[attr-defined]
    builtins.input.assert_called_once_with(  # type: ignore[attr-defined]
        "move file.0010.txt -> newfile.10.txt? (y/n): "
    )  # type: ignore[attr-defined]
