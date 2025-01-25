import typer

from typing import Optional
import jig.cmds.project
import jig.cmds.app


cli = typer.Typer()


@cli.command()
def project(
    name: str,
    target: str = ".",
    app: Optional[str] = typer.Option(None),
    lib: Optional[str] = typer.Option(None),
    namespace: Optional[str] = typer.Option(""),
):

    pj = jig.cmds.project.Project(name)
    pj.generate(target)

    # run_copy(
    #     template,
    #     output_dir,
    #     data={
    #         "module_namespace": namespace,
    #         "module_name": name,
    #         "module_namespace_snk": to_snake_case(namespace),
    #         "module_name_snk": to_snake_case(name),
    #     },
    #     skip_if_exists=["__init__.py"],
    # )

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
    app = jig.cmds.app.App(name)
    app.generate(target)


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
