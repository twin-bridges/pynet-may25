#!/usr/bin/env python
"""
Create a Python script that does the following:
a. Prompts a user for a first_name and a last_name.
b. Use an f-string to print out these names.
c. Print out the names using an f-string with columns 30 wide and the names right aligned.
d. Print out the names using an f-string with columns 30 wide and the names center aligned. 
e. Print out the first name variable and value using an f-string and the '{f_name = }' technique.

Example running script:

----------
$ python exercise5.py

### Part 'a':
Enter your first name: Kirk
Enter your last name: Byers

### Part 'b' (print the name):
Kirk Byers

### Part 'c' (30 width columns, right-aligned):
                          Kirk                          Byers

### Part 'd' (30 width columns, centered):
             Kirk                          Byers

### Part 'e' ({var = } technique):
first_name = 'Kirk'
----------

"""

print("\n### Part 'a': ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("\n### Part 'b' (print the name): ")
print(f"{first_name} {last_name}")

print("\n### Part 'c' (30 width columns, right-aligned): ")
print(f"{first_name:>30} {last_name:>30}")

print("\n### Part 'd' (30 width columns, centered): ")
print(f"{first_name:^30} {last_name:^30}")

print("\n### Part 'e' ({var = } technique): ")
print(f"{first_name = }")

