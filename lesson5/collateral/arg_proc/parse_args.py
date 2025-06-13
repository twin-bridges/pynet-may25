#!/usr/bin/env python
import argparse
from rich import print

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
parser.add_argument(
    "-c",
    "--connect",
    help="Automatically Connect",
    dest="create_conn",
    action="store_true",
    default=False,
)

cli_args = parser.parse_args()
print(cli_args)

hostname = cli_args.hostname
print(f"{hostname =}")
