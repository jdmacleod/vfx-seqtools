"""Tests for the vfx-seqtools seqrm CLI utility."""

import pathlib

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
