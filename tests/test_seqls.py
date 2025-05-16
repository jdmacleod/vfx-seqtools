"""Tests for the vfx-seqtools seqls CLI utility."""

import glob

import fileseq
from pytest_mock import MockFixture
from typer.testing import CliRunner

from vfx_seqtools.seqls_cli import app

runner = CliRunner(mix_stderr=False)

test_files = [
    "file.0001.exr",
    "file.0002.exr",
    "file.0003.exr",
    "file.0004.exr",
    "file.0005.exr",
]

test_missing_files = [
    "missingfile.0001.exr",
    "missingfile.0002.exr",
    "missingfile.0003.exr",
    "missingfile.0005.exr",
]


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


def test_seqls_calls_glob_with_pattern(mocker: MockFixture) -> None:
    """Test that the seqls command calls glob when a pattern is provided."""
    mocker.patch("glob.glob", return_value=test_files)
    mocker.patch("fileseq.findSequencesInList", return_value="file.1-5#.exr")
    result = runner.invoke(app, ["*.exr"])
    assert result.exit_code == 0
    glob.glob.assert_called_once_with("*.exr")  # type: ignore[attr-defined]
    fileseq.findSequencesInList.assert_called_once_with(test_files)


def test_seqls_calls_fileseq_without_pattern(mocker: MockFixture) -> None:
    """Test that the seqls command calls fileseq when no pattern is provided."""
    mocker.patch("fileseq.findSequencesOnDisk", return_value=test_files)
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    fileseq.findSequencesOnDisk.assert_called_once_with(".")


def test_seqls_honors_missing_frame_option(mocker: MockFixture) -> None:
    """Test that the seqls command honors the missing frame option."""
    mocker.patch("glob.glob", return_value=test_missing_files)
    result = runner.invoke(app, ["*.exr", "-m"])
    assert result.exit_code == 0
    glob.glob.assert_called_once_with("*.exr")  # type: ignore[attr-defined]
    assert "Missing frames: 0004" in result.stdout
