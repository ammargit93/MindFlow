from typing import List
import random
import yaml
import os

def load_config(config_path: str = None):
    if config_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        config_path = os.path.join(base_dir, "config.yml")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    return config

    