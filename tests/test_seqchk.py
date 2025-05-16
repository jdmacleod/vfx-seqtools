"""Tests for the vfx-seqtools seqchk CLI utility."""

import glob
import logging

import fileseq
import OpenEXR
import PIL
import PIL.Image
import pytest
from pytest_mock import MockFixture
from typer.testing import CliRunner

from vfx_seqtools.seqchk_cli import app

runner = CliRunner(mix_stderr=False)


test_files = [
    "file.0001.exr",
    "file.0002.exr",
    "file.0003.exr",
    "file.0004.exr",
    "file.0005.exr",
]


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


def test_seqchk_calls_glob_with_pattern(mocker: MockFixture) -> None:
    """Test that the seqchk command calls glob when a pattern is provided."""
    mocker.patch("glob.glob", return_value=test_files)
    mocker.patch("fileseq.findSequencesInList", return_value="file.1-5#.exr")
    result = runner.invoke(app, ["*.exr"])
    assert result.exit_code == 0
    glob.glob.assert_called_once_with("*.exr")  # type: ignore[attr-defined]
    fileseq.findSequencesInList.assert_called_once_with(test_files)


def test_seqchk_calls_fileseq_without_pattern(mocker: MockFixture) -> None:
    """Test that the seqchk command calls fileseq when no pattern is provided."""
    mocker.patch("fileseq.findSequencesOnDisk", return_value=test_files)
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    fileseq.findSequencesOnDisk.assert_called_once_with(".")


def test_seqchk_calls_pillow(mocker: MockFixture) -> None:
    """Test that the seqchk command calls pillow to check an image."""
    mocker.patch("PIL.Image.open", return_value=True)
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    PIL.Image.open.assert_called()


def test_seqchk_calls_openexr(mocker: MockFixture) -> None:
    """Test that the seqchk command calls openexr to check an exr image."""
    mocker.patch("glob.glob", return_value=test_files)
    mocker.patch("OpenEXR.File", return_value=True)
    result = runner.invoke(app, ["*.exr"])
    assert result.exit_code == 0
    OpenEXR.File.assert_called()


def test_seqchk_honors_dry_run_with_exr(
    mocker: MockFixture, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the seqchk command honors dry-run option."""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    mocker.patch("glob.glob", return_value=test_files)
    mocker.patch("fileseq.findSequencesInList", return_value=[test_files])
    mocker.patch("OpenEXR.File", return_value=True)
    result = runner.invoke(app, ["*.exr", "-n"])
    assert result.exit_code == 0
    OpenEXR.File.assert_not_called()  # type: ignore[attr-defined]
    assert result.stdout == ""
    assert "dry-run: CHECK" in caplog.text
    caplog.clear()


def test_seqchk_honors_verbose_option_with_exr(
    mocker: MockFixture, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the seqmv command honors verbose option."""
    caplog.set_level(
        logging.INFO, logger="rich"
    )  # Set the rich caplog level to INFO and above
    mocker.patch("glob.glob", return_value=test_files)
    mocker.patch("OpenEXR.File", return_value=True)
    result = runner.invoke(app, ["*.exr", "--verbose"])
    assert result.exit_code == 0
    glob.glob.assert_called_once_with("*.exr")  # type: ignore[attr-defined]
    OpenEXR.File.assert_called()
    assert "CHECK file.0005.exr" in caplog.text
    caplog.clear()
