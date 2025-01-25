import typer
import jig.create

app = typer.Typer()
app.add_typer(jig.create.cli, name="create")


def main_cli():
    app()


main_cli()
