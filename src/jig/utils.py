import os
import re


def find_config_file(filename="jig.yml"):
    # search in local working dir first
    local_path = os.path.join(os.getcwd(), filename)
    if os.path.isfile(local_path):
        return local_path

    # search in $HOME/.config/jig
    home_config_dir = os.path.join(os.getenv("HOME", ""), ".config", "jig")
    config_path = os.path.join(home_config_dir, filename)
    if os.path.isfile(config_path):
        return config_path

    # Todo: if no config file found create on
    return None


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def camel_to_upper(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).upper()
