"""
Repeat exercise1 except store your "vmx1" information in a dictionary and pass that
information into ConnectHandler using the **kwargs technique.
"""
import os
from netmiko import ConnectHandler

password = os.environ["NETMIKO_PASSWORD"]

vmx1 = {
    "device_type": "juniper_junos",
    "host": "vmx1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

ssh = ConnectHandler(**vmx1)
print(f"\nDevice Prompt: {ssh.find_prompt()}\n")
ssh.disconnect()
