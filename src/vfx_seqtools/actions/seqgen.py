import logging
from typing import Annotated

import fileseq
import typer

from vfx_seqtools import common_options
from vfx_seqtools.decorators import attach_hook


def to_list(frames: str) -> list:
    """Return a list from a passed string of frame numbers.

    Args:
        frames (str): the frame numbers, comma or space-separated.

    Returns:
        list: list representation of the numbers.
    """
    if "," in frames:
        return [int(i) for i in frames.split(",")]
    elif " " in frames:
        return [int(i) for i in frames.split()]
    else:
        return [int(i) for i in frames.split(",")]


@attach_hook(common_options.logging_options, hook_output_kwarg="logger")
@attach_hook(common_options.version_option, hook_output_kwarg="show_version")
def seqgen(
    frames: Annotated[
        str,
        typer.Argument(
            help="A list of frames to consider, ex. '1,3,5,7'. Use quotes to surround space-separated values."
        ),
    ],
    show_version: bool,
    logger: logging.Logger,
) -> None:
    """
    Generate a frame sequence from individual frame numbers.

    'seqgen 1,3,5,7' - will return the frame sequence 1-7x2.
    """
    framelist = to_list(frames)
    seq = fileseq.FrameSet(framelist)

    print(seq.frange)
