import yaml

from pathlib import Path
from jig.utils import find_config_file
from git import Repo

from copier import run_copy


class Project:
    def __init__(self, name):
        self.template = None
        self.name = name

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
        print(jig_config)

    def generate(self, target):
        print(f"Creating project: {self.name} in {target}")
        project_template = f"{self.template}/cpp/project"
        run_copy(project_template, target, data={"project_name": self.name})
