import django
from django.core.exceptions import ValidationError
from rich import print
from netmiko import ConnectHandler
from getpass import getpass

django.setup()

from net_db.models import DNSServer, NetworkDevice  # noqa


def device_connect(net_object, password):
    print(f"\nConnecting to {net_object.host}\n")
    ssh_conn = ConnectHandler(
        host=net_object.host,
        device_type=net_object.device_type,
        username=net_object.username,
        password=password,
    )
    return ssh_conn


if __name__ == "__main__":

    password = getpass()

    cf_dns = DNSServer.objects.filter(provider="Cloudflare")
    if len(cf_dns) != 2:
        count = len(cf_dns)
        msg = f"Expected exactly two DNS servers and {count} returned"
        raise ValidationError(msg)

    cfg_lines = []
    dns_servers = []
    for dns_obj in cf_dns:
        cfg_line = f"set system name-server {dns_obj.ip_addr}"
        cfg_lines.append(cfg_line)
        dns_servers.append(dns_obj.ip_addr)

    print()
    print("Configuration to send: ")
    print("-" * 50)
    print(cfg_lines)
    print("-" * 50)
    print()

    vmx_devices = NetworkDevice.objects.filter(name__contains="vmx")
    for device in vmx_devices:
        ssh_conn = device_connect(device, password)

        print("Configuring DNS Servers: ")
        output = ssh_conn.send_config_set(cfg_lines)
        print("-" * 50)
        print(output)
        print("-" * 50)
        output = ssh_conn.commit()

        # Junos requires config mode for this command:
        ssh_conn.config_mode()
        current_dns = ssh_conn.send_command("show system name-server")

        for dns_srv in dns_servers:
            print(f"Verify configuration: {dns_srv}")
            assert dns_srv in current_dns

        print()
