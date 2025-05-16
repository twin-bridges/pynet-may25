import csv
from rich import print

with open("net_devices.csv") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        print(row)
