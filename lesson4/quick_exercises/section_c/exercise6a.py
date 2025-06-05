"""
Create a Python script that does the following:

a. Use a for loop to connect to both "vmx1" and "vmx2" via SSH. "vmx2" is identical to "vmx1"
   (see exercise1 in this section) except its hostname is "vmx2.lasthop.io".

b. Use Netmiko's send_command() method to execute "show arp" on both of these devices.

c. Create an "output_dict" to store the results of the show command. The dictionary keys should
   be the two device names: "vmx1" and "vmx2". The corresponding value should be the "show arp"
   output.

d. After you are completely done capturing the output, then loop over your "output_dict" and
   print out both the device name and corresponding "show arp" output.

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
