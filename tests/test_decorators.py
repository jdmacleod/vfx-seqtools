from vfx_seqtools import decorators


def a_test_hook_func(a_hook_value: str) -> str:
    """A test hook function."""
    return f"hook rv: {a_hook_value}"


@decorators.attach_hook(
    a_test_hook_func,
    hook_output_kwarg="hook_output",
)
def a_test_func(
    a_value: str,
    b_value: str,
    c_value: str,
    hook_output: str,
) -> str:
    """A test function."""
    return f"func rv: {a_value} {b_value} {c_value} {hook_output}"


def test_hook_output_passed_to_source() -> None:
    """Test that the hook function output is passed to the source function."""
    value_c = "value_c"
    value_a = 1
    value_b = "value b"
    a_hook_value = "hook value"
    expected = f"func rv: {value_a} {value_b} {value_c} hook rv: {a_hook_value}"
    result = a_test_func(value_a, value_b, value_c, a_hook_value=a_hook_value)
    assert result == expected, f"Expected: {expected}, but got: {result}"
