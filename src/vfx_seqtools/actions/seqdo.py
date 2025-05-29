import logging
import subprocess
from typing import Annotated, Optional

import fileseq
import typer
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)

from vfx_seqtools import common_options
from vfx_seqtools.decorators import attach_hook
from vfx_seqtools.parser import replace_hash_and_at_with_framenumber


def do_action(tupl: tuple) -> None:
    cmds, frame, is_dryrun, be_verbose, be_strict, logger = tupl
    substituted_cmds = replace_hash_and_at_with_framenumber(cmds, frame)
    if is_dryrun:
        logger.info(f"dry-run: {substituted_cmds}")
    else:
        # Run the command using subprocess or any other method
        if be_verbose:
            logger.info(f"{substituted_cmds}")

        try:
            subprocess.run(substituted_cmds, shell=True)
        except Exception as e:
            if be_strict:
                raise
            logger.warning(
                f"Command failed: {substituted_cmds}, skipping it. Use --strict to stop on errors. {e}"
            )


@attach_hook(common_options.dry_run_option, hook_output_kwarg="is_dryrun")
@attach_hook(common_options.frame_range_options, hook_output_kwarg="frame_range")
@attach_hook(common_options.frame_seq_options, hook_output_kwarg="frame_seq")
@attach_hook(common_options.logging_options, hook_output_kwarg="logger")
@attach_hook(common_options.verbose_option, hook_output_kwarg="be_verbose")
@attach_hook(common_options.strict_option, hook_output_kwarg="be_strict")
@attach_hook(common_options.version_option, hook_output_kwarg="show_version")
def seqdo(
    cmds: Annotated[
        str, typer.Argument(help="The command(s) to run. Use quotes to group commands.")
    ],
    logger: logging.Logger,
    be_verbose: Optional[bool] = False,
    be_strict: Optional[bool] = False,
    frame_range: tuple[int, int, int] = (0, 0, 0),
    frame_seq: str = "",
    is_dryrun: Optional[bool] = False,
    show_version: Optional[bool] = False,
) -> None:
    """
    Do command(s) for the provided framerange. Use '@' and '#' to specify frame numbers in the command.

    For example, 'echo @' will print the frame number, and 'echo file.#.exr' will print the file name with the frame number.

    Use 'seqdo "echo @" -f 1-5' to print the frame number for each frame in the range 1-5.

    Use 'seqdo "echo file.####.exr" -f 6-10' to print the file name with the frame number (4-padded) for each frame in the range 6-10.
    """
    if frame_seq:
        frames = fileseq.FrameSet(frame_seq)
    elif frame_range[0] != 0 or frame_range[1] != 0:
        frames = fileseq.FrameSet(f"{frame_range[0]}-{frame_range[1]}x{frame_range[2]}")
    else:
        frames = []

    if is_dryrun:
        for frame in frames:
            do_action((cmds, frame, is_dryrun, be_verbose, be_strict, logger))
    else:
        from rich.logging import RichHandler

        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(rich_tracebacks=True)],
        )
        logger = logging.getLogger("rich")
        progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            MofNCompleteColumn(),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
        )
        with progress:
            for frame in progress.track(frames, description="Working..."):
                do_action((cmds, frame, is_dryrun, be_verbose, be_strict, logger))
