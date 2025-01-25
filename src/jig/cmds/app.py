import yaml

from pathlib import Path
from jig.utils import find_config_file
from git import Repo

from copier import run_copy


class App:
    def __init__(self, name):
        self.template = None
        self.name = name.lower()

        jig_config_file = find_config_file()
        with open(jig_config_file, "r") as fh:
            jig_config = yaml.safe_load(fh)

        tmpl_url = jig_config["jig"]["template"]["source"]["url"]
        local_templ_path = jig_config["jig"]["template"]["source"]["dest"]

        if not Path(local_templ_path).is_dir():
            Path(local_templ_path).mkdir(parents=True)
            repo = Repo()
            repo.clone_from(tmpl_url, local_templ_path)

        self.template = local_templ_path

    def generate(self, target):
        print(f"Creating App: {self.name} in {target}")
        project_template = f"{self.template}/cpp/app"
        run_copy(
            project_template,
            target,
            data={"appname": self.name, "appname_lcase": self.name.lower()},
        )
        # append to CMakeLists.txt
        parent_cmake = f"{target}/CMakeLists.txt"
        if Path(parent_cmake).is_file():
            print(f"writing to: {parent_cmake}")
            with open(parent_cmake, "a") as fh:
                fh.write(f"add_subdirectory(app_{self.name})\n")
