"""
Using the SR OS data structure from exercise1, create a Python script that converts the original
data structure to:

{'slot1': {'mda1': 's36-100gb-qsfp28'}}

Print this new data structure out to standard output.
"""
from rich import print

# Original SR OS data structure
data = {
    "nokia-conf:configure": {
        "card": [
            {
                "slot-number": 1,
                "mda": [{"mda-slot": 1, "mda-type": "s36-100gb-qsfp28"}],
                "fp": [{"fp-number": 1}, {"fp-number": 2}],
            }
        ]
    }
}

config = data["nokia-conf:configure"]

modules = config["card"]
modules = modules[0]

slot_number = modules["slot-number"]
slot_one = modules["mda"][0]
mda_slot_number = slot_one["mda-slot"]
mda_card_type = slot_one["mda-type"]

new_dict = {f"slot{slot_number}": {f"mda{slot_number}": mda_card_type}}

print(new_dict)
