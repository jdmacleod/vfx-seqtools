"""Tests for the vfx-seqtools seqchk CLI utility."""

import PIL
import PIL.Image
from pytest_mock import MockFixture
from typer.testing import CliRunner

from vfx_seqtools.seqchk_cli import app

runner = CliRunner(mix_stderr=False)


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


def test_seqchk_calls_pillow(mocker: MockFixture) -> None:
    """Test that the seqchk command calls pillow to check an image."""
    mocker.patch("PIL.Image.open", return_value=True)
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    PIL.Image.open.assert_called()
