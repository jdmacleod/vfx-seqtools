"""CLI wrapper for seqdo."""

import typer

from vfx_seqtools.actions.seqdo import seqdo

app = typer.Typer()

app.command()(seqdo)


if __name__ == "__main__":
    app()
