from typing import Optional
import typer
from typing_extensions import Annotated

import word2md.word2md
from word2md import __app_name__, __version__
from pathlib import Path
from spire.doc import *
from spire.doc.common import *


app = typer.Typer()

@app.command()
def convert(source: Annotated[
    str,
    typer.Option(
    "--source",
    "-s",
    prompt = "The path of the source word document",
    help = "The path of the source word document to convert"
    ),
], target: Annotated[
    str,
    typer.Option(
        "--target",
        "-t",
        prompt="The path of the target MD document",
        help="The path of the converted target MD document"
    ),
]) -> None:
    """ initializes the to-do database """
    # Create a Document object
    document = Document()
    source_doc = Path(source)
    target_doc = Path(target)
    # Load a Word file
    document.LoadFromFile(str(source_doc))
    # Save it as an MD file
    document.SaveToFile(str(target_doc), FileFormat.Markdown)
    # Dispose resources
    document.Dispose()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


def main(version: Annotated[
    Optional[bool],
    typer.Option("--version",
                 "-v",
                 help="Show the application's version and exit.",
                 callback=_version_callback,
                 is_eager=True, )
] = None) -> None:
    """ main entry point to the application """
    return