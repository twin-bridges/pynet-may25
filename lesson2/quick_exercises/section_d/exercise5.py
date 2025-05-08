from pathlib import Path

current_dir = Path.cwd()


def read_file(file_name, file_path=current_dir):
    full_path = file_path / file_name
    if full_path.is_file():
        with open(full_path) as f:
            return f.read()


# Test reading using defaults
# data = read_file(file_name="local.ini")

# Test reading using a constructed path
home_dir = Path.home()
test_path = home_dir / Path("pynet-may25/lesson2/quick_exercises/section_d")
data = read_file(file_name="local.ini", file_path=test_path)
print()
print("File Contents:")
print("-" * 40)
print(data)
print("-" * 40)
print()
