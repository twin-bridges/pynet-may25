"""
Using your data_centers dictionary from exercise1, create a Python script where you:
a. Loop over this dictionary and print out all of the keys (the data-center names).
b. Loop over this dictionary and print out all of the key-value pairs (the data-center
   names and corresponding addresses).
"""

data_centers = {
    "sf1": "200 Paul Ave",
    "sf2": "1 King Street",
    "sf3": "365 Main Street",
    "la1": "1 Wilshire Blvd.",
    "la2": "50 W. Hollywood Blvd.",
}

# Part a.
print()
for dc_name in data_centers:
    print(f"Data Center Name: {dc_name}")
print()

# Part b.
print()
for dc_name, dc_address in data_centers.items():
    print(f"{dc_name} --> {dc_address}")
print()
