import dataclasses
import os
from typing import Optional

from trycortex.cli import utils

@dataclasses.dataclass
class CallableConfig(utils.DataClassYamlMixin):
    # Represents an callable.yaml config file
    name: str = "callable"
    description: str = ""
    visibility: str = "private"
    template: str = "barbone"
    entry_point: str = "main:callable"
    sID: str = ""

def normalize_path(path: Optional[str] = None) -> str:
    """Normalizes paths to an CallableConfig.

    Args:
        path: Optional path to either a directory or YAML file. If unspecified,
            will return "callable.yaml".
    """
    if not path:
        path = "callable.yaml"
    elif os.path.isdir(path):
        path = os.path.join(path, "callable.yaml")

    return path

def load_config(path: Optional[str] = None) -> CallableConfig:
    """Loads CallableConfig from the given path, or its default path.

    Args:
        path: Optional path to load config from. By default, config is loaded from
            "{cwd}/callable.yaml".
    """
    path = normalize_path(path)
    with open(path, "r") as fp:
        return CallableConfig.from_yaml(fp)

def save_config(callable_config: CallableConfig, path: Optional[str] = None):
    """Saves the given CallableConfig to the given path, or its default path.

    Args:
        callable_config: The CallableConfig object to save into file.
        path: Optional path to save. By default, it's saved to the default path at
            "{cwd}/callable.yaml".
    """
    path = normalize_path(path)
    with open(path, "w") as fp:
        fp.write(callable_config.to_yaml())