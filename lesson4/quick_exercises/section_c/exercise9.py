import os
from rich import print
from netmiko import ConnectHandler


def find_current_dns(ssh_conn):
    """
    Find the currently configured DNS servers on a Junos Device.

    Return a list of name-servers.
    """
    current_ns = ssh_conn.send_command("show configuration system name-server")
    current_ns = current_ns.splitlines()
    dns_servers = []
    for ns in current_ns:
        ns = ns.strip()
        # Strip off trailing ';'
        ns = ns.rstrip(";")
        dns_servers.append(ns)

    return dns_servers


if __name__ == "__main__":

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
    current_nservers = find_current_dns(ssh_conn)
    # Delete any extra name-servers
    for ns in current_nservers:
        if ns not in name_servers:
            cmd = f"{base_delete_cmd} {ns}"
            commands.append(cmd)

    output = ssh_conn.send_config_set(commands)
    output += ssh_conn.commit()
    print(output)
    ssh_conn.disconnect()
