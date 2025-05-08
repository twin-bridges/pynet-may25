"""
In a Python script create the following dictionary of dictionaries:

data_centers = {
    "sf1": {
        "address": "200 Paul St.",
        "network_prefix": "172.20.0.0/20",
        "site_contact": "john.doe@gmail.com",
    },
    "la1": {
        "address": "1 Wilshire Blvd.",
        "network_prefix": "172.21.0.0/20",
        "site_contact": "jane.smith@gmail.com",
    },
}

Given the above:
a. Print out the inner-dictionary that is associated with the "sf1" key.
b. Print out the "address" of the "sf1" data center.
c. Loop over the data_centers dictionary and print out the data_center name and its
   "network_prefix"

"""
from rich import print

data_centers = {
    "sf1": {
        "address": "200 Paul St.",
        "network_prefix": "172.20.0.0/20",
        "site_contact": "john.doe@gmail.com",
    },
    "la1": {
        "address": "1 Wilshire Blvd.",
        "network_prefix": "172.21.0.0/20",
        "site_contact": "jane.smith@gmail.com",
    },
}

# Part a.
print()
print(data_centers["sf1"])

# Part b.
print()
print(f'SF1 Address: {data_centers["sf1"]["address"]}')

# Part c.
print()
print(f"{'dc_name':10} {'network_prefix':16}")
print(f"{'-' * 10} {'-' * 16}")
for dc_name, dc_data in data_centers.items():
    network_prefix = dc_data["network_prefix"]
    print(f"{dc_name:10} {network_prefix:16}")
print()
