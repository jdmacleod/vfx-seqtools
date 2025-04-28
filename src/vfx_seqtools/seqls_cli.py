"""CLI wrapper for seqls."""

import typer

from vfx_seqtools.actions.seqls import seqls

app = typer.Typer()

app.command()(seqls)


if __name__ == "__main__":
    app()
