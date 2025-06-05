import yaml
from rich import print
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from netmiko import ConnectHandler

MAX_THREADS = 10


def read_netmiko_yml():
    home = Path.home()
    netmiko_yml = home / ".netmiko.yml"

    with open(netmiko_yml) as f:
        return yaml.safe_load(f)


def ssh_conn(device_name, device_dict, cmd):
    """Create a Netmiko connection and execute 'cmd', return a tuple of (device_name, output)."""
    with ConnectHandler(**device_dict) as net_connect:
        output = net_connect.send_command(cmd)
        return (device_name, output)


def main():

    device_data = read_netmiko_yml()
    cisco_grp = device_data["cisco"]
    arista_grp = device_data["arista"]
    juniper_grp = device_data["juniper"]
    all_devices = cisco_grp + arista_grp + juniper_grp

    pool = ThreadPoolExecutor(MAX_THREADS)
    future_work = []
    cmd_table = {
        "juniper_junos": "show interfaces terse",
        "cisco_ios": "show ip interface brief",
        "arista_eos": "show ip interface brief",
    }

    for device_name in all_devices:
        device_dict = device_data[device_name]

        # Look up the proper command based on the platform
        device_type = device_dict["device_type"]
        cmd = cmd_table[device_type]

        if "vmx" in device_name:
            cmd = f"{cmd} | match fxp0.0"
        elif "srx" in device_name:
            cmd = f"{cmd} | match vlan.0"

        # Create a 'future' i.e. work-to-be-done
        future = pool.submit(
            ssh_conn,
            device_name=device_name,
            device_dict=device_dict,
            cmd=cmd,
        )
        future_work.append(future)

    for future in as_completed(future_work):
        # Retrieve the 'result' from the future (tuple returned by 'ssh_conn')
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()


if __name__ == "__main__":
    main()
