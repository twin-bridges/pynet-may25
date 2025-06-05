"""
Create a Netmiko script that connects to "vmx1" (info below):

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass
  password: <invalid>

After you have established an SSH connection with this device, use the Netmiko find_prompt()
method and print out the device's prompt to standard output.

You should NOT hard-code the password in the script, instead read the password in from an
environment variable.

You can set an environment variable (in the lab environment) using the following:

export NETMIKO_PASSWORD=fake_password         # Password Provided separately

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
