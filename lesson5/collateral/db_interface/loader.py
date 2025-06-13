import yaml
from rich import print
from pathlib import Path
import django

django.setup()

from net_db.models import NetworkDevice, Interface  # noqa


def read_netmiko_yml():
    home = Path.home()
    netmiko_yml = home / ".netmiko.yml"

    with open(netmiko_yml) as f:
        return yaml.safe_load(f)


def create_django_obj(name, host, device_type, username):
    nd = NetworkDevice(
        name=name,
        host=host,
        device_type=device_type,
        username=username,
    )
    nd.save()
    return nd


if __name__ == "__main__":

    nd = NetworkDevice.objects.all()
    print(nd)

    net_devices = read_netmiko_yml()

    cisco_grp = net_devices["cisco"]
    arista_grp = net_devices["arista"]
    juniper_grp = net_devices["juniper"]
    all_devices = cisco_grp + arista_grp + juniper_grp

    for device_name in all_devices:
        device_dict = net_devices[device_name]
        device_dict.pop("password")
        if device_dict.get("global_delay_factor"):
            device_dict.pop("global_delay_factor")
        device_dict["name"] = device_name
        nd = create_django_obj(**device_dict)
        print(nd)

    cisco3 = NetworkDevice.objects.get(name="cisco3")

    for intf_name in ("GigabitEthernet0/0/0", "GigabitEthernet0/0/1"):
        intf = Interface(
            device=cisco3,
            intf_name=intf_name,
            intf_type="1000BaseT"
        )
        intf.save()
        print(intf) 
