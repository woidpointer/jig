import yaml

from pathlib import Path
from jig.utils import find_config_file, camel_to_upper, camel_to_snake
from git import Repo

from copier import run_copy


class Cpp:
    def __init__(self, name, namespace):
        self.template = None
        self.namespace = namespace.lower()
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

    def generate(self, target):
        print(f"Creating Lib: {self.name} in {target}")
        project_template = f"{self.template}/cpp/class"
        run_copy(
            project_template,
            target,
            data={
                "class": camel_to_snake(self.name),
                "namespace": self.namespace,
                "namespace_list": self._namespace_list(),
                "namespace_rlist": self._namespace_rlist(),
                "include_guard": self._include_guard(),
                "include_path": self._include_path(),
                "Class": self.name,
            },
        )

    def _namespace_list(self):
        return list(self.namespace.split("::"))

    def _namespace_rlist(self):
        return list(reversed(self._namespace_list()))

    def _include_guard(self):
        guard_list = []

        if not (
            len(self._namespace_list()) == 1 and self._namespace_list()[0] == ""
        ):
            guard_list += self._namespace_list()

        guard_list.append(camel_to_upper(self.name))
        guard_list.append("HPP")

        return str("_".join(guard_list)).upper()

    def _include_path(self):
        include_list = []

        if not (
            len(self._namespace_list()) == 1 and self._namespace_list()[0] == ""
        ):
            include_list += self._namespace_list()

        include_list.append(camel_to_snake(self.name) + ".hpp")
        return "/".join(include_list)
