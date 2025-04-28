"""CLI wrapper for seqchk."""

import typer

from vfx_seqtools.actions.seqchk import seqchk

app = typer.Typer()

app.command()(seqchk)


if __name__ == "__main__":
    app()
