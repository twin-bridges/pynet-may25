"""
a. Use a for loop to connect via SSH to both "vmx1" and "vmx2".

b. Use Netmiko's send_command() method to execute "show arp | display json" on both of these
   devices (that is the "pipe" character after "show arp").

c. The 'show arp | display json' command will return a JSON data structure as a string. Use
   the 'json' library to convert this string to a Python data structure.

d. The returned data structure will be fairly complex, use your complex data structure process
   from class3 to extract all of the ARP entries from both "vmx1" and "vmx2". The extraction
   process should retrieve the 'ip_addr', the 'mac_addr', and the 'interface'.

e. Print each ARP entry out to standard output. Your output should look similar to the
   following (note, some of the ARP entries might be different/missing).

$ python exercise6b.py

vmx1:
-----
128.0.0.16 --> 02:00:00:00:00:10 (em1.0)
172.30.0.1 --> 06:ec:49:d0:bd:27 (fxp0.0)
172.30.0.219 --> 06:1a:97:b0:c4:89 (fxp0.0)

vmx2:
-----
128.0.0.16 --> 02:00:00:00:00:10 (em1.0)
172.30.0.1 --> 06:ec:49:d0:bd:27 (fxp0.0)

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
