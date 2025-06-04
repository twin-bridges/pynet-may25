"""
Repeat exercise1 except with the "session_log" enabled. View the session_log after your
script has executed.
"""
import os
from netmiko import ConnectHandler

password = os.environ["NETMIKO_PASSWORD"]

ssh = ConnectHandler(
    device_type="juniper_junos",
    host="vmx1.lasthop.io",
    username="pyclass",
    password=password,
    session_log="vmx1.txt",
)
print(f"\nDevice Prompt: {ssh.find_prompt()}\n")
ssh.disconnect()
