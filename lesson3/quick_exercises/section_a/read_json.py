import json
from rich import print


with open("nokia_sros.json") as f:
    data = json.load(f)

print(data)
