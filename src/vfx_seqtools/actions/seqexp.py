import logging
from typing import Annotated

import fileseq
import typer

from vfx_seqtools import common_options
from vfx_seqtools.decorators import attach_hook


def pad_frame(frame: int, pad: int = 0) -> str:
    """Return a padded frame number.

    Args:
        frame (int): the frame number to pad
        pad (int): the number of zeros to pad the frame number with

    Returns:
        str: string representation of the number - padded or unpadded.
    """
    # handle padding for negative numbers
    if frame < 0:
        pad = pad + 1 if pad else 0
    return f"{frame:0{pad}d}" if pad else str(frame)


@attach_hook(common_options.logging_options, hook_output_kwarg="logger")
@attach_hook(common_options.version_option, hook_output_kwarg="show_version")
def seqexp(
    frameseq: Annotated[
        str, typer.Argument(help="A frame sequence to expand, ex. 1-10x3.")
    ],
    show_version: bool,
    logger: logging.Logger,
    pad: Annotated[
        int,
        typer.Option(
            "--pad",
            "-p",
            help="List frame numbers with zero padding, number of zeros to pad.",
        ),
    ] = 0,
    long_list: Annotated[
        bool,
        typer.Option(
            "--long-list",
            "-l",
            help="Long listing of frame numbers, one per line.",
        ),
    ] = False,
) -> None:
    """
    Expand a frame sequence to individual frame numbers - quickly evaluate a frame sequence.

    'seqexp 1-10x3' - will expand the frame sequence to 1 4 7 10.
    """
    seq = fileseq.FrameSet(frameseq)

    if long_list:
        for frame in seq:
            print(pad_frame(frame, pad))
    else:
        print(" ".join(str(pad_frame(frame, pad)) for frame in seq))
