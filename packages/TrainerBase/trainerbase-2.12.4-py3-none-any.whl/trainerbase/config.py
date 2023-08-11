from tomllib import load as load_toml
from pathlib import Path


with Path("./trainerbase.toml").resolve().open("rb") as trainerbase_toml:
    trainerbase_config = load_toml(trainerbase_toml)


pymem_config = trainerbase_config["pymem"]
