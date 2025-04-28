import logging
import shutil
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
    src, dst, frame, is_dryrun, be_verbose, be_interactive, be_strict, logger = tupl
    substituted_src = replace_hash_and_at_with_framenumber(src, frame)
    substituted_dst = replace_hash_and_at_with_framenumber(dst, frame)
    if is_dryrun:
        logger.info(f"dry-run: MOVE {substituted_src} {substituted_dst}")
    else:
        if be_verbose:
            logger.info(f"MOVE: {substituted_src} {substituted_dst}")
        try:
            if be_interactive:
                confirm = input(f"move {substituted_src} -> {substituted_dst}? (y/n): ")
                if confirm.lower() != "y":
                    return
            shutil.move(substituted_src, substituted_dst)
        except Exception as e:
            if be_strict:
                raise
            logger.warning(
                f"Error moving file: {substituted_src} -> {substituted_dst}, skipping it. Use --strict to stop on errors. {e}"
            )


@attach_hook(common_options.dry_run_option, hook_output_kwarg="is_dryrun")
@attach_hook(common_options.frame_range_options, hook_output_kwarg="frame_range")
@attach_hook(common_options.frame_seq_options, hook_output_kwarg="frame_seq")
@attach_hook(common_options.logging_options, hook_output_kwarg="logger")
@attach_hook(common_options.threading_option, hook_output_kwarg="thread_count")
@attach_hook(common_options.interactive_option, hook_output_kwarg="be_interactive")
@attach_hook(common_options.verbose_option, hook_output_kwarg="be_verbose")
@attach_hook(common_options.strict_option, hook_output_kwarg="be_strict")
@attach_hook(common_options.version_option, hook_output_kwarg="show_version")
def seqmv(
    src: Annotated[str, typer.Argument(help="The source name pattern for the frames.")],
    dst: Annotated[
        str, typer.Argument(help="The destination name pattern for the frames.")
    ],
    logger: logging.Logger,
    be_verbose: Optional[bool] = False,
    be_strict: Optional[bool] = False,
    be_interactive: Optional[bool] = False,
    frame_range: tuple[int, int, int] = (0, 0, 0),
    frame_seq: str = "",
    is_dryrun: Optional[bool] = False,
    show_version: Optional[bool] = False,
    thread_count: Optional[int] = 0,
) -> None:
    """
    Move(rename) files from <SRC> to <DST>, using the provided framerange.
    """
    if frame_seq:
        frames = fileseq.FrameSet(frame_seq)
    elif frame_range[0] != 0 or frame_range[1] != 0:
        print(f"frame_range: {frame_range}")
        frames = fileseq.FrameSet(f"{frame_range[0]}-{frame_range[1]}x{frame_range[2]}")
    else:
        frames = []

    if is_dryrun:
        for frame in frames:
            do_action(
                (
                    src,
                    dst,
                    frame,
                    is_dryrun,
                    be_verbose,
                    be_interactive,
                    be_strict,
                    logger,
                )
            )
    else:
        # skip progress bar if interactive
        if be_interactive:
            for frame in frames:
                do_action(
                    (
                        src,
                        dst,
                        frame,
                        is_dryrun,
                        be_verbose,
                        be_interactive,
                        be_strict,
                        logger,
                    )
                )
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
                    do_action(
                        (
                            src,
                            dst,
                            frame,
                            is_dryrun,
                            be_verbose,
                            be_interactive,
                            be_strict,
                            logger,
                        )
                    )
