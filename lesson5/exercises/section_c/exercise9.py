from lxml import etree
from rich import print

my_xml = etree.parse("junos_show_arp.xml")

xml_root = my_xml.getroot()

arp_ip_addresses = xml_root.findall(".//{*}ip-address")

print()
print("IP Addresses in the ARP Table:")
print("-" * 50)
for ip_addr in arp_ip_addresses:
    print(ip_addr.text)
print()
