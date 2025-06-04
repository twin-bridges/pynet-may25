from pathlib import Path
from rich import print

cwd = Path.cwd()
new_dirs = cwd / "tmp_dir1/test1/test2"
new_dirs.mkdir(parents=True, exist_ok=True)

print(f"\n{new_dirs} exists: {new_dirs.exists()}")
print(f"{new_dirs} is directory: {new_dirs.is_dir()}\n")
