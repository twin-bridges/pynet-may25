"""
Create a Python script that uses pathlib. The script should create a Path object representing
your "home" directory (this directory can be determined from the Linux shell by typing 'cd ~').

a. Using the home_dir Path object, create a new Path object for "python-libs". This is a
   subdirectory of "home". Using pathlib verify this directory exists and is a directory.

b. Using the "python-libs" object, create a new Path object corresponding to the "snmp_helper.py"
   file (which exists inside of the "python-libs" directory). Use pathlib to verify this file
   exists and is a file.

"""
from pathlib import Path
from rich import print

home_dir = Path.home()
python_libs = home_dir / "python-libs"

print(f"\n{python_libs} exists: {python_libs.exists()}")
print(f"{python_libs} is directory: {python_libs.is_dir()}")

snmp_file = python_libs / "snmp_helper.py"
print(f"\n{snmp_file} exists: {snmp_file.exists()}")
print(f"{snmp_file} is file: {snmp_file.is_file()}\n")
