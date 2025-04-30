"""Tests for the vfx-seqtools seqmv CLI utility."""

import shutil

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


def test_seqmv_honors_dry_run(mocker: MockFixture) -> None:
    """Test that the seqmv command honors dry-run option."""
    mocker.patch("shutil.move", return_value=True)
    result = runner.invoke(app, ["file.####.txt", "newfile.@.txt", "-f", "10-10", "-n"])
    assert result.exit_code == 0
    shutil.move.assert_not_called()  # type: ignore[attr-defined]
