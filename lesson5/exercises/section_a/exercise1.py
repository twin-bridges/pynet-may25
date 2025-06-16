#!/usr/bin/env python
import argparse
from rich import print
from netmiko import ConnectHandler
from getpass import getpass

parser = argparse.ArgumentParser(description="Show Version Utility")
parser.add_argument("hostname", help="Hostname", action="store", type=str)
parser.add_argument(
    "-d",
    "--device_type",
    help="Device Type",
    action="store",
    type=str,
    default="juniper_junos",
)
parser.add_argument(
    "-u", "--username", help="Username", action="store", type=str, required=True
)

cli_args = parser.parse_args()

password = getpass()
hostname = cli_args.hostname
device_type = cli_args.device_type
username = cli_args.username

print()
print(f"'show version' output for {hostname}")
print("-" * 50)
with ConnectHandler(
    host=hostname, device_type=device_type, username=username, password=password
) as nc:
    output = nc.send_command("show version")
    print(output)
print("-" * 50)
print()
