"""
Create a Python script that has the following data structure (a list of lists):

data_centers = [
    ["sf1", "10.100.0.0/20"],
    ["sf2", "10.100.16.0/20"],
    ["la1", "10.100.32.0/20"],
]

In this script use an f-string to print out the Los Angeles data center name and its IP
prefix.

"""

data_centers = [
    ["sf1", "10.100.0.0/20"],
    ["sf2", "10.100.16.0/20"],
    ["la1", "10.100.32.0/20"],
]

site_name = data_centers[2][0]
site_prefix = data_centers[2][1]

out_data = f"""

Site Name: {site_name}
Site Prefix: {site_prefix}

"""
print(out_data)
