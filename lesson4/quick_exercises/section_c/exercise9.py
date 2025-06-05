import os
from rich import print
from netmiko import ConnectHandler

password = os.environ["NETMIKO_PASSWORD"]

vmx2 = {
    "device_type": "juniper_junos",
    "host": "vmx2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

name_servers = [
    "1.1.1.1",
    "1.0.0.1",
]

base_add_cmd = "set system name-server"
base_delete_cmd = "delete system name-server"
commands = []
for ns in name_servers:
    cmd = f"{base_add_cmd} {ns}"
    commands.append(cmd)

ssh_conn = ConnectHandler(**vmx2)
current_nservers = ssh_conn.send_command("show configuration system name-server")
current_nservers = current_nservers.splitlines()
for ns in current_nservers:
    ns = ns.strip()
    # Strip off trailing ';'
    ns = ns.rstrip(";")
    # Delete any extra name-servers
    if ns not in name_servers:
        cmd = f"{base_delete_cmd} {ns}"
        commands.append(cmd)

print(commands)
ssh_conn.disconnect()
