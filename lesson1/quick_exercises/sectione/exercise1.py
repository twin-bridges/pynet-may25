#!/usr/bin/env python
"""
a. Open a file named "some_file.txt" for reading. This file will need to be in the same
   directory as your program and have some text in it. Read this file using the '.read()'
   method. Make sure the file is properly closed. Print the file contents out to standard
   output.

b. Open the file named "some_file.txt" for reading again. This time read the file using the
   .readlines() method. Print the results from .readlines() out to standard output (this
   should be a list that contains all the lines of the file).

"""

# Part "a" ####

# No context manager
f = open("some_file.txt")
# .read() will return the entire file contents as a string.
data = f.read()
f.close()

print(f"\nEx1a:\n\n{data}\n\n")


# Part "b" ####
# See video5 on File Context Managers for reference (you could also just .open() and
# .close() the file, as done in part 'a').

# Using a context manager
with open("some_file.txt") as f:
    # .readlines() will return a list of lines (in the file)
    data = f.readlines()

print(f"Ex1b:\n\n{data}\n\n")
