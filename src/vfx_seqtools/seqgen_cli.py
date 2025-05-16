"""CLI wrapper for seqgen."""

import typer

from vfx_seqtools.actions.seqgen import seqgen

app = typer.Typer()

# We use `ignore_unknown_options` to allow passing negative numbers in the frame range.
# otherwise, the CLI would interpret the negative number in the range '-5-10' as an option.
# https://github.com/fastapi/typer/discussions/798
app.command(context_settings={"ignore_unknown_options": True})(seqgen)


if __name__ == "__main__":
    app()
