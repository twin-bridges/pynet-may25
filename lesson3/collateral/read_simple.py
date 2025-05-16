import csv
from rich import print

with open('net_devices.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
