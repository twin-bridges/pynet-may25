"""
Repeat exercise1 except store your "vmx1" information in a dictionary and pass that
information into ConnectHandler using the **kwargs technique.
"""
import os
from netmiko import ConnectHandler
from rich import print

password = os.environ["NETMIKO_PASSWORD"]

vmx1 = {
    "device_type": "juniper_junos",
    "host": "vmx1.lasthop.io",
    "username": "pyclass",
    "password": password,
}
vmx2 = {
    "device_type": "juniper_junos",
    "host": "vmx2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

out_dict = {}
for device in (vmx1, vmx2):
    with ConnectHandler(**device) as ssh_conn:
        hostname = device["host"]
        # Use only the first field of the hostname
        hostname = hostname.split(".")[0]
        output = ssh_conn.send_command("show arp")
        out_dict[hostname] = output

print()
for hostname, output in out_dict.items():
    print(f"\n>>> {hostname} output:\n\n{output}")
print()
