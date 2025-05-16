import yaml
from rich import print


def read_yaml_file(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    filename = input("Enter filename: ")

    yaml_data = read_yaml_file(filename)
    print(yaml_data)
