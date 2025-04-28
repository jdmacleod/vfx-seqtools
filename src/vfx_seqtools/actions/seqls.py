import glob
import logging
from typing import Annotated

import fileseq
import typer

from vfx_seqtools import common_options
from vfx_seqtools.decorators import attach_hook


@attach_hook(common_options.logging_options, hook_output_kwarg="logger")
@attach_hook(common_options.version_option, hook_output_kwarg="show_version")
@attach_hook(common_options.sequence_only_option, hook_output_kwarg="only_on_sequences")
def seqls(
    show_version: bool,
    logger: logging.Logger,
    filepattern: Annotated[
        str,
        typer.Argument(
            help="An optional file pattern to use, use quotes or escape shell wildcards like '?' and '*'."
        ),
    ] = "",
    only_on_sequences: bool = False,
) -> None:
    """
    List file sequences.

    seqls - will list all file sequences in the current directory.

    seqls file.\*.exr - will list all file sequences matching the pattern 'file.*.exr' (escaping shell wildcards).

    seqls "file.????.exr" - will list all file sequences matching the pattern 'file.????.exr' (quoting shell wildcards).

    """
    if filepattern:
        files = glob.glob(filepattern)
        seqs = fileseq.findSequencesInList(files)
    else:
        seqs = fileseq.findSequencesOnDisk(".")

    for seq in seqs:
        if only_on_sequences and "@" not in str(seq) and "#" not in str(seq):
            continue
        print(f"{seq}")
