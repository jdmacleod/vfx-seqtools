import re


def replace_hash_and_at_with_framenumber(
    input_string: str,
    number: int,
) -> str:
    """
    Replace '#' and '@' in the input string with integers.

    '#' and '@' are replaced with the value of `number`,
    """

    def zero_padded_match(match: re.Match) -> str:
        offset_match = re.match(r"(#+)([+-])(\d+)", match.group(0))
        if offset_match:
            offset = int(offset_match.group(3))
            offset = abs(offset) if offset_match.group(2) == "+" else -abs(offset)
            padding_length = len(offset_match.group(1))
            # account for negative numbers and formatting
            if number + offset < 0:
                padding_length += 1
            return f"{(number + offset):0{padding_length}}"
        else:
            padding_length = len(match.group(0))
            # account for negative numbers and formatting
            if number < 0:
                padding_length += 1
            return f"{number:0{padding_length}}"

    def unpadded_match(match: re.Match) -> str:
        offset_match = re.match(r"(@+)([+-])(\d+)", match.group(0))
        if offset_match:
            offset = int(offset_match.group(3))
            offset = abs(offset) if offset_match.group(2) == "+" else -abs(offset)
            return str(number + offset)
        else:
            return str(number)

    # Replace '#' and '@' with the frame number
    output_string = re.sub(r"(#+)([+-]\d+)?", zero_padded_match, input_string)
    output_string = re.sub(r"(@+)([+-]\d+)?", unpadded_match, output_string)

    return output_string
