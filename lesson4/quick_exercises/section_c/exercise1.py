"""
Create a Netmiko script that connects to "vmx1" (info below):

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass
  password: <invalid>

After you have established an SSH connection with this device, use the find_prompt() and
print the device's prompt to standard output.

You should NOT hard-code the password in the script, instead read the password in from an
environment variable.

You can set an environment variable using (using the shell in the lab environment):

export NETMIKO_PASSWORD=<invalid>         # Provided separately

"""
import os
from netmiko import ConnectHandler

password = os.environ["NETMIKO_PASSWORD"]

ssh = ConnectHandler(
    device_type="juniper_junos",
    host="vmx1.lasthop.io",
    username="pyclass",
    password=password,
)
print(f"\nDevice Prompt: {ssh.find_prompt()}\n")
ssh.disconnect()
