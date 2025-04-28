"""CLI wrapper for seqcp."""

import typer

from vfx_seqtools.actions.seqcp import seqcp

app = typer.Typer()

app.command()(seqcp)


if __name__ == "__main__":
    app()
