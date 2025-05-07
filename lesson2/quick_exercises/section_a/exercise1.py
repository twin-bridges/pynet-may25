#!/usr/bin/env python
"""
Create a Python script that uses the following email address: "paul.atreides@gmail.com":

a. Using string methods, create three variables from this email address: first_name,
   last_name, domain_name.

b. Check that the domain name is "gmail.com" and print a message if this is found.

c. Check that the first_name is "paul" and the last_name is "atreides" and print a message
   if this is found.
"""

email_address = "paul.atreides@gmail.com"

# Part a.
# Split on the '@' sign
name, domain_name = email_address.lower().split("@")
first_name, last_name = name.split(".")

# Part b.
if domain_name == "gmail.com":
    print(f"\nFound the correct domain name: {domain_name}")

# Part c.
if first_name == "paul" and last_name == "atreides":
    print(f"\nFound the correct name: {first_name} {last_name}")
