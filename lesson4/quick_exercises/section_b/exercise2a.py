"""
Create a Python script that finds your current working directory.

From this directory use "pathlib" to create the following directories "tmp_dir1/test1/test2".
This directory structure should relative to your current working directory.

After you have created this directory structure use the .exists() and is_dir() methods to
verify this structure now exists and is a directory.

"""
from pathlib import Path
from rich import print

cwd = Path.cwd()
new_dirs = cwd / "tmp_dir1/test1/test2"
new_dirs.mkdir(parents=True, exist_ok=True)

print(f"\n{new_dirs} exists: {new_dirs.exists()}")
print(f"{new_dirs} is directory: {new_dirs.is_dir()}\n")
