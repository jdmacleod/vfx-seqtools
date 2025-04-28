import logging
import pathlib
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
    src, frame, is_dryrun, be_verbose, be_interactive, be_strict, logger = tupl
    substituted_src = replace_hash_and_at_with_framenumber(src, frame)
    if is_dryrun:
        logger.info(f"dry-run: DELETE {substituted_src}")
    else:
        if be_verbose:
            logger.info(f"DELETE: {substituted_src}")
        try:
            if be_interactive:
                confirm = input(f"delete {substituted_src}? (y/n): ")
                if confirm.lower() != "y":
                    return
            pathlib.Path.unlink(pathlib.Path(substituted_src))
        except Exception as e:
            if be_strict:
                raise
            logger.warning(
                f"Error deleting file: {substituted_src}, skipping it. Use --strict to stop on errors. {e}"
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
def seqrm(
    src: Annotated[str, typer.Argument(help="The files to remove.")],
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
    Remove files with pattern <SRC>, using the provided framerange.

    Use 'seqrm file.####.exr -f 1-5' to remove file.0001.exr through file.0005.exr.

    """
    if frame_seq:
        frames = fileseq.FrameSet(frame_seq)
    elif frame_range[0] != 0 or frame_range[1] != 0:
        frames = fileseq.FrameSet(f"{frame_range[0]}-{frame_range[1]}x{frame_range[2]}")
    else:
        frames = []

    if is_dryrun:
        for frame in frames:
            do_action(
                (src, frame, is_dryrun, be_verbose, be_interactive, be_strict, logger)
            )
    else:
        # skip progress bar if interactive
        if be_interactive:
            for frame in frames:
                do_action(
                    (
                        src,
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
                            frame,
                            is_dryrun,
                            be_verbose,
                            be_interactive,
                            be_strict,
                            logger,
                        )
                    )
