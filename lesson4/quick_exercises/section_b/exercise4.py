"""
Create a Python script that uses "os.system" to execute "ping -c 3 127.0.0.1".

This will ping localhost three times. Save the return value from this command and verify
the command executes successfully. The return value should be zero, if the command is
successful.

You should see these pings on standard output when you execute your Python script.

"""
import os

ping_cmd = "ping -c 3 127.0.0.1"
ret_val = os.system(ping_cmd)

if ret_val == 0:
    print("Command successful!")
