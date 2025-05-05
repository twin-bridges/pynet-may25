#!/usr/bin/env python
"""
Open a file
Read a file using f.read()
Read a file using f.readlines()
"""

# No context manager
f = open("some_file.txt")
# .read() will return the entire file contents as a string.
data = f.read()
f.close()

print(f"\nEx1a:\n\n{data}\n\n")

# Using a context manager
with open("some_file.txt") as f:
    # .readlines() will return a list of lines (in the file)
    data = f.readlines()

print(f"Ex1b:\n\n{data}\n\n")
