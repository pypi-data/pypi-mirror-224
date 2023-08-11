from pathlib import Path
from shutil import copytree


copytree(Path(__file__).resolve().parent / "template", Path("."), dirs_exist_ok=True)
