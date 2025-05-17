import csv
from rich import print

with open("people.csv", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        print(row)
