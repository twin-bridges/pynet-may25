#!/usr/bin/env python
"""
a. Write "hello world\n" out to a file named "test_file.txt". Properly open and close the
   file and ensure the file contents have been properly written.

Contents after part a:
------
# Execute script
$ python exercise2a.py

# Verify file has been created.
$ ls
exercise1.py  exercise2a.py  some_file.txt  test_file.txt

# Verify file contents.
$ cat test_file.txt
hello world
------

"""

file_name = "test_file.txt"
data = "hello world\n"

# No context manager
f = open(file_name, mode="w")
f.write(data)
f.close()
