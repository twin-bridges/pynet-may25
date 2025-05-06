# /usr/bin/env python
"""
b. Create a Python script that does the following:
   i.  Create a Windows Path named "C:\windows\new_dir\test_me" using raw strings.
   ii. Print this Windows Path out to standard output and verify that it is correct
       (i.e. that \n and \t work properly and are literal characters).


### Example executing script:
---------
$ python exercise6b.py

Windows Path: C:\windows\new_dir\test_me

---------
"""

windows_path = r"C:\windows\new_dir\test_me"
print(f"\nWindows Path: {windows_path}\n\n")
