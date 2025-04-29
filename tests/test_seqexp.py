"""Tests for the vfx-seqtools seqexp CLI utility."""

import pytest
from typer.testing import CliRunner

from vfx_seqtools.seqexp_cli import app

runner = CliRunner(mix_stderr=False)


testdata = [
    ("1-5", "1 2 3 4 5\n", "1\n2\n3\n4\n5\n"),
    ("1-5,7-9", "1 2 3 4 5 7 8 9\n", "1\n2\n3\n4\n5\n7\n8\n9\n"),
    ("1-10x3", "1 4 7 10\n", "1\n4\n7\n10\n"),
    ("10-20y5", "11 12 13 14 16 17 18 19\n", "11\n12\n13\n14\n16\n17\n18\n19\n"),
    ("3-10:3", "3 6 9 5 7 4 8 10\n", "3\n6\n9\n5\n7\n4\n8\n10\n"),
    ("-3-5", "-3 -2 -1 0 1 2 3 4 5\n", "-3\n-2\n-1\n0\n1\n2\n3\n4\n5\n"),
]

testdata_padded = [
    ("1-5", 4, "0001 0002 0003 0004 0005\n", "0001\n0002\n0003\n0004\n0005\n"),
    (
        "1-5,7-9",
        3,
        "001 002 003 004 005 007 008 009\n",
        "001\n002\n003\n004\n005\n007\n008\n009\n",
    ),
    ("1-10x3", 2, "01 04 07 10\n", "01\n04\n07\n10\n"),
    ("10-20y5", 0, "11 12 13 14 16 17 18 19\n", "11\n12\n13\n14\n16\n17\n18\n19\n"),
    ("3-10:3", 1, "3 6 9 5 7 4 8 10\n", "3\n6\n9\n5\n7\n4\n8\n10\n"),
    (
        "-3-5",
        2,
        "-03 -02 -01 00 01 02 03 04 05\n",
        "-03\n-02\n-01\n00\n01\n02\n03\n04\n05\n",
    ),
]


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "vfx-seqtools, version" in result.stdout


@pytest.mark.parametrize("input_string, expected_compact, expected_long", testdata)
def test_seqexp_expands_list_compact(
    input_string: str, expected_compact: str, expected_long: str
) -> None:
    """Test that the seqexp command expands a list compactly."""
    result = runner.invoke(app, [input_string])
    assert result.exit_code == 0
    assert result.stdout == expected_compact


@pytest.mark.parametrize("input_string, expected_compact, expected_long", testdata)
def test_seqexp_expands_list_long(
    input_string: str, expected_compact: str, expected_long: str
) -> None:
    """Test that the seqexp command expands a list in long format."""
    result = runner.invoke(app, [input_string, "-l"])
    assert result.exit_code == 0
    assert result.stdout == expected_long


@pytest.mark.parametrize(
    "input_string, padding, expected_compact, expected_long", testdata_padded
)
def test_seqexp_expands_list_compact_padded(
    input_string: str, padding: int, expected_compact: str, expected_long: str
) -> None:
    """Test that the seqexp command expands a list compactly, with padding."""
    result = runner.invoke(app, [input_string, "-p", str(padding)])
    assert result.exit_code == 0
    assert result.stdout == expected_compact


@pytest.mark.parametrize(
    "input_string, padding, expected_compact, expected_long", testdata_padded
)
def test_seqexp_expands_list_long_padded(
    input_string: str, padding: int, expected_compact: str, expected_long: str
) -> None:
    """Test that the seqexp command expands a list in long format, with padding."""
    result = runner.invoke(app, [input_string, "-l", "-p", str(padding)])
    assert result.exit_code == 0
    assert result.stdout == expected_long
