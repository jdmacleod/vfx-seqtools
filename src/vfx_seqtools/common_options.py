import logging
import pathlib
from typing import Annotated, Optional

import typer

from vfx_seqtools import __version__


def version_callback(value: bool) -> None:
    """Display the version of the package."""
    if value:
        typer.echo(f"vfx-seqtools, version {__version__}")
        raise typer.Exit()


def version_option(
    version: bool = typer.Option(
        False,
        "--version",
        is_eager=True,
        help="Show the version of the package.",
        callback=version_callback,
    ),
) -> None:
    """Utilities for working with VFX frame sequences."""
    pass


def dry_run_option(
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            "-n",
            help="Show what would be done, but do not do it.",
        ),
    ] = False,
) -> bool:
    return dry_run


def logging_options(
    log_level: Annotated[
        int,
        typer.Option(help="Log level. Must be a Python log level (10,20,30,40,50)."),
    ] = logging.INFO,
    log_to_file: Annotated[
        Optional[pathlib.Path], typer.Option(help="A file to stream logs to.")
    ] = None,
) -> logging.Logger:
    logger = logging.getLogger("vfx_seqtools")
    logger.setLevel(log_level)
    # set a simple format for basic logging

    if log_level <= 20:
        formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    if log_to_file:
        file_handler = logging.FileHandler(log_to_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger


def interactive_option(
    interactive: Annotated[
        Optional[bool],
        typer.Option(
            "--interactive",
            "-i",
            help="Request confirmation before attempting to act on each file.",
        ),
    ] = False,
) -> Optional[bool]:
    return interactive


def verbose_option(
    verbose: Annotated[
        Optional[bool],
        typer.Option(
            "--verbose",
            "-v",
            help="Be verbose when acting, showing actions as they are taken.",
        ),
    ] = False,
) -> Optional[bool]:
    return verbose


def strict_option(
    strict: Annotated[
        Optional[bool],
        typer.Option(help="Be strict; stop on errors."),
    ] = False,
) -> Optional[bool]:
    return strict


def quiet_option(
    quiet: Annotated[
        Optional[bool],
        typer.Option("--quiet", "-q", help="Be quiet; produce minimal output."),
    ] = False,
) -> Optional[bool]:
    return quiet


def sequence_only_option(
    only_sequences: Annotated[
        Optional[bool],
        typer.Option(
            "--only-sequences",
            "-o",
            help="Only consider sequences; ignore non-sequence files.",
        ),
    ] = False,
) -> Optional[bool]:
    return only_sequences


def missing_frames_option(
    missing_frames: Annotated[
        Optional[bool],
        typer.Option(
            "--missing-frames",
            "-m",
            help="Show missing frames in sequences.",
        ),
    ] = False,
) -> Optional[bool]:
    return missing_frames


def frame_range_options(
    frame_start: Annotated[
        int,
        typer.Option("--frame-start", "-fs", help="frame start. must be an integer."),
    ] = 0,
    frame_end: Annotated[
        int, typer.Option("--frame-end", "-fe", help="frame end. must be an integer.")
    ] = 0,
    frame_increment: Annotated[
        Optional[int],
        typer.Option(
            "--frame-increment",
            "-fi",
            help="frame increment. optional, must be an integer, default=1.",
        ),
    ] = 1,
) -> tuple[int, int, Optional[int]]:
    return frame_start, frame_end, frame_increment


def frame_seq_options(
    frameseq: Annotated[
        str,
        typer.Option(
            "--frame-seq", "-f", help="A frame sequence to expand, ex. 1-10x3."
        ),
    ] = "",
) -> Optional[str]:
    return frameseq


def threading_option(
    threads: Annotated[
        Optional[int],
        typer.Option(
            "--threads",
            "-t",
            help="Number of threads to use; default=0 (all threads). Negative integers will use all but n threads.",
        ),
    ] = 0,
) -> Optional[int]:
    return threads
