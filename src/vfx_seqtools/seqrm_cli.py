"""CLI wrapper for seqcp."""

import typer

from vfx_seqtools.actions.seqrm import seqrm

app = typer.Typer()

app.command()(seqrm)


if __name__ == "__main__":
    app()
