"""
Create a Python script that reads this JSON file:

nokia_sros.json

Use rich.print to print this data structure out. In Python, the outermost data structure
should be a dictionary.
"""
import json
from rich import print

with open("nokia_sros.json", encoding="utf-8") as f:
    nokia_config = json.load(f)

print(nokia_config)
