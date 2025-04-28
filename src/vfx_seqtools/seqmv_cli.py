"""CLI wrapper for seqmv."""

import typer

from vfx_seqtools.actions.seqmv import seqmv

app = typer.Typer()

app.command()(seqmv)


if __name__ == "__main__":
    app()
