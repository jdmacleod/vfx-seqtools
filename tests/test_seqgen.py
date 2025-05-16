"""Tests for the vfx-seqtools seqgen CLI utility."""

import pytest
from typer.testing import CliRunner

from vfx_seqtools.seqgen_cli import app

runner = CliRunner(mix_stderr=False)


testdata = [
    ("1-5\n", "1 2 3 4 5\n", "1,2,3,4,5\n"),
    ("1-5,7-9\n", "1 2 3 4 5 7 8 9\n", "1,2,3,4,5,7,8,9\n"),
    ("1-10x3\n", "1 4 7 10\n", "1,4,7,10\n"),
    ("-3-5\n", "-3 -2 -1 0 1 2 3 4 5\n", "-3,-2,-1,0,1,2,3,4,5\n"),
    ("-3-11x2\n", "-3 -1 1 3 5 7 9 11\n", "-3,-1,1,3,5,7,9,11\n"),
]


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


@pytest.mark.parametrize("expected_string, input_spaces, input_commas", testdata)
def test_seqgen_handles_spaces(
    expected_string: str, input_spaces: str, input_commas: str
) -> None:
    """Test that the seqgen command generates a sequence from a space-separated set of framenumbers."""
    result = runner.invoke(app, [input_spaces])
    assert result.exit_code == 0
    assert result.stdout == expected_string


@pytest.mark.parametrize("expected_string, input_spaces, input_commas", testdata)
def test_seqgen_handles_commas(
    expected_string: str, input_spaces: str, input_commas: str
) -> None:
    """Test that the seqgen command generates a sequence from a comma-separated set of framenumbers."""
    result = runner.invoke(app, [input_commas])
    assert result.exit_code == 0
    assert result.stdout == expected_string
