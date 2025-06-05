import csv

data = [
    {
        "device_name": "cisco3",
        "device_type": "cisco_ios",
        "host": "cisco3.invalid.com",
        "username": "admin",
        "password": "cisco123",
        "port": "",
        "global_delay_factor": "",
    },
    {
        "device_name": "cisco4",
        "device_type": "cisco_ios",
        "host": "cisco4.invalid.com",
        "username": "admin",
        "password": "cisco123",
        "port": "",
        "global_delay_factor": "",
    },
]
# Use one of the dictionaries (key-names) to extract the header row
header = list(data[0].keys())

filename = "outfile.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:

    csv_wr = csv.DictWriter(f, fieldnames=header)

    # Header row
    csv_wr.writeheader()
    for row in data:
        csv_wr.writerow(row)

    # Alternate solution
    # csv_wr.writerows(data)
