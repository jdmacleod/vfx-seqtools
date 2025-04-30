"""Tests for the vfx-seqtools seqdo CLI utility."""

import subprocess

from pytest_mock import MockFixture
from typer.testing import CliRunner

from vfx_seqtools.seqdo_cli import app

runner = CliRunner(mix_stderr=False)


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


def test_seqdo_calls_subprocess_run_with_shell_true(mocker: MockFixture) -> None:
    """Test that the seqdo command calls subprocess to run commands."""
    mocker.patch("subprocess.run", return_value=True)
    result = runner.invoke(app, ["echo file.###.tif", "-f", "10-10"])
    assert result.exit_code == 0
    subprocess.run.assert_called_once_with("echo file.010.tif", shell=True)  # type: ignore[attr-defined]


def test_seqdo_honors_dry_run(mocker: MockFixture) -> None:
    """Test that the seqdo command honors dry-run option."""
    mocker.patch("subprocess.run", return_value=True)
    result = runner.invoke(app, ["echo file.####.txt", "-f", "10-10", "-n"])
    assert result.exit_code == 0
    subprocess.run.assert_not_called()  # type: ignore[attr-defined]
