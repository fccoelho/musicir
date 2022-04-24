"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Music Information Retrieval."""


if __name__ == "__main__":
    main(prog_name="musicir")  # pragma: no cover
