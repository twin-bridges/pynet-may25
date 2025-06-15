#!/usr/bin/env python
import argparse
from rich import print
import os

password = os.environ["NETMIKO_PASSWORD"]

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
print(cli_args)

hostname = cli_args.hostname
device_type = cli_args.device_type
username = cli_args.username

nc = ConnectHandler(host=hostname, device_type=device_type, username=username, password=password)
print(f"{hostname =}")
print(f"{device_type=}")
print(f"{username=}")
print(f"{password=}")
