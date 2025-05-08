from pathlib import Path

current_dir = Path.cwd()


def read_file(file_name, file_path=current_dir):
    full_path = file_path / file_name
    if full_path.is_file():
        with open(full_path) as f:
            return f.read()


data = read_file(file_name="local.ini")
print()
print("File Contents:")
print("-" * 40)
print(data)
print("-" * 40)
print()
