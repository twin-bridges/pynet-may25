#!/usr/bin/env python
"""
Create a Python script that contains a list of five email addresses:
a. Using a for-loop verify that each email address contains the '@' symbol. If you encounter
   an email address without the '@' sign, use 'continue' to cease processing on that email
   address.

b. Still inside the for-loop from Part b, add a check for one particular email address. If
   this email address is encountered, then break out of the for-loop.

c. At the end of the for-loop print out the email address.
"""

email_addresses = [
    "paul.atreides@gmail.com",
    "duncan.idaho@gmail.com",
    "baron.harkonnen@gmail.com",
    "chani.kynes@gmail.com",
    "invalid.email",
]

print()
for email in email_addresses:
    # Part a.
    if "@" not in email:
        continue

    # Part b.
    if "chani.kynes@gmail.com" in email.lower():
        break

    # Part c.
    print(email)
print()

# Alternate solution using if/elif/else (since this pattern works as well)
print()
print("Alternate solution: ")
print()
for email in email_addresses:
    if "@" not in email:
        # Part a.
        continue
    elif "chani.kynes@gmail.com" in email.lower():
        # Part b.
        break
    else:
        # Part c.
        print(email)
print()
