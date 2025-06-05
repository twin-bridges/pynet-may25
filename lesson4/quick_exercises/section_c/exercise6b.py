"""
Repeat exercise1 except store your "vmx1" information in a dictionary and pass that
information into ConnectHandler using the **kwargs technique.
"""
import os
import json
from rich import print
from netmiko import ConnectHandler

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
        data = ssh_conn.send_command("show arp | display json")
        arp_dict = json.loads(data)
        arp_table = arp_dict["arp-table-information"][0]
        arp_entries = arp_table["arp-table-entry"]

        print(f"\n{hostname}:")
        print("-----")
        for entry in arp_entries:
            mac_addr = entry["mac-address"][0]["data"]
            ip_addr = entry["ip-address"][0]["data"]
            intf = entry["interface-name"][0]["data"]
            print(f"{ip_addr} --> {mac_addr} ({intf})")

print()
