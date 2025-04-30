"""Tests for the vfx-seqtools seqcp CLI utility."""

import shutil

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
