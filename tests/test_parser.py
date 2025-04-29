"""Tests for the frame token parsing."""

import pytest

from vfx_seqtools.parser import replace_hash_and_at_with_framenumber

testdata = [
    ("frame.##.exr", 5, "frame.05.exr"),
    ("frame.##+1.exr", 5, "frame.06.exr"),
    ("frame.###-2.exr", 5, "frame.003.exr"),
    ("frame.####-7.exr", 5, "frame.-0002.exr"),
    ("file##.exr", -9, "file-09.exr"),
    ("frame.@@.exr", 5, "frame.5.exr"),
    ("frame.@@+1.exr", 5, "frame.6.exr"),
    ("frame.@@-4.exr", 5, "frame.1.exr"),
    ("frame.@@-6.exr", 5, "frame.-1.exr"),
]


@pytest.mark.parametrize("input_string, number, expected", testdata)
def test_parser_replaces_tokens_and_offsets(
    input_string: str, number: int, expected: str
) -> None:
    """Test that the parser replaces hash and at with correct values, honoring offsets."""
    result = replace_hash_and_at_with_framenumber(input_string, number)
    assert result == expected
