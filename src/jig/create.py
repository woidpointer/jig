import typer
from typing import Optional
from jig.utils import find_config_file

cli = typer.Typer()


@cli.command()
def project(
    name: str,
    target: str = ".",
    amsr_app: Optional[str] = typer.Option(None),
    app: Optional[str] = typer.Option(None),
    lib: Optional[str] = typer.Option(None),
    namespace: Optional[str] = typer.Option(""),
):

    jig_config = find_config_file()
    print(jig_config)

    print(f"Creating project: {name} in {target}")

    # prj = Project(name, target)
    # prj.create()

    # if app:
    #     app_target_path = f"{target}/{name}/sources"
    #     app_creator = App(app, App.Type.GENERIC)
    #     app_creator.create(app_target_path)

    # if amsr_app:
    #     app_target_path = f"{target}/{name}/sources"
    #     app_creator = App(amsr_app, App.Type.AMSR)
    #     app_creator.create(app_target_path)

    # if lib:
    #     lib_target_path = f"{target}/{name}/sources"
    #     lib_creator = Lib(lib, namespace)
    #     lib_creator.create(lib_target_path)


@cli.command()
def app(name: str, target: str = "."):
    print(f"Creating app: {name} in {target}")


@cli.command()
def lib(name: str, target: str = ".", namespace: str = ""):
    print(f"Creating lib: {name} in {target}")


@cli.command()
def cpp(name: str, target: str = ".", namespace: str = ""):
    print(f"Creating cpp: {name} in {target} ns: {namespace}")


def main():
    cli()


if __name__ == "__main__":
    main()
