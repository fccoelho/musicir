"""Command-line interface."""
import click
from musicir.leadsheets.musicxml import HarmonyParser
from pprint import pprint

@click.command()
@click.version_option()
@click.argument('filename', type=click.File('r'))
def main(filename: str) -> None:
    """Music Information Retrieval.
    Extract the harmony from leadsheets, in musicxml format.
    returning it as a JSON array.

    FILENAME is the leadsheet from which the harmony is to be extracted.
    """
    H = HarmonyParser(filename)
    click.echo(H.as_json())


if __name__ == "__main__":
    main(prog_name="musicir")  # pragma: no cover
