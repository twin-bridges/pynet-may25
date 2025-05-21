"""
Create a Python Script that reads in the below CSV file. It should read this file in using
the CSV library and the DictReader class.

show_ip_int_br.csv

After the CSV is read in, use rich.print and a for-loop to print out all of the 
dictionaries that are returned.
"""
import csv
from rich import print

with open("show_ip_int_br.csv") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        print(row)
