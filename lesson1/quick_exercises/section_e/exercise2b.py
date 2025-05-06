#!/usr/bin/env python
"""

b. Repeat this process again, once again writing to a file name "text_file.txt". This time
   write the text "some text\n" out to the file. Verify that the original file was completely
   overwritten by the new text.

Contents after part b:
-------
# Contents of the file before executing 'exercise2b.py'
$ cat test_file.txt
hello world

$ python exercise2b.py

# New contents have completely replaced the old contents.
$ cat test_file.txt
some text
-------

"""

# See video5 on 'File Context Managers' for reference (you could also just .open() and
# .close() the file, as done in part 'a').
file_name = "test_file.txt"
data = "some text\n"
with open(file_name, mode="w") as f:
    f.write(data)
