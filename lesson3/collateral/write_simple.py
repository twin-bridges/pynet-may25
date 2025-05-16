import csv

# List of lists
data = [
    [
        "device_name",
        "device_type",
        "host",
        "username",
        "password",
        "port",
        "global_delay_factor",
    ],
    ["cisco3", "cisco_ios", "cisco3.invalid.com", "admin", "cisco123", "", ""],
    ["cisco4", "cisco_ios", "cisco4.invalid.com", "admin", "cisco123", "", ""],
]

with open("my_file.csv", "w", newline="") as f:
    csv_wr = csv.writer(f)

    for row in data:
        csv_wr.writerow(row)
