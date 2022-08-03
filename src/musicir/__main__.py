"""Command-line interface."""
from pprint import pprint

import click

from musicir.leadsheets.musicxml import SongParser


@click.command()
@click.version_option()
# @click.option('-h')
# @click.option('-m')
@click.argument("filename", type=click.File("r"))
def main(filename: str) -> None:
    """Music Information Retrieval.
    Extract the harmony from leadsheets, in musicxml format.
    returning it as a JSON array.

    FILENAME is the leadsheet from which the harmony is to be extracted.
    """
    S = SongParser(filename)
    click.echo(S.chords_as_json())


if __name__ == "__main__":
    main(prog_name="musicir")  # pragma: no cover
