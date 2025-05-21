"""
Using the "get" retrieval process constructed in the previous exercise, retrieve the
following url:

url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"

This will retrieve the IP addresses / network blocks stored in NetBox (there aren't very many
of them). Analyze the returned data structure and determine how many IP address blocks were
returned (remember your Complex Data Structure Process from Class2). From the returned data
structure find the IP address block "10.199.0.0/21".

From this "10.199.0.0/21" address block retrieve the following information and print it to
 standard output: object 'id', URL, address-family name (use the 'family', 'label' fields).
"""

import os
import requests
from rich import print


from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


TOKEN = os.environ["NETBOX_TOKEN"]

HTTP_HEADERS = {"accept": "application/json"}
if TOKEN:
    HTTP_HEADERS["authorization"] = "Token {}".format(TOKEN)


def retrieve_url(url):
    # verify=False (self-signed SSL certificate) - this is insecure/not appropriate
    # for production use.
    response = requests.get(url, headers=HTTP_HEADERS, verify=False)
    return response.json()


if __name__ == "__main__":

    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
    data = retrieve_url(url)

    count = data["count"]
    print()
    print(f"Total Prefixes/IP Address Objects Retrieved: {count}\n")

    results = data["results"]
    for entry in results:
        if entry.get("address", "") == "10.199.0.0/21":
            ip_block = entry
            break

    print(f"IP Prefix Address: {ip_block['address']}")

    print(f"IP Prefix ID: {ip_block['id']}")
    print(f"IP Prefix URL: {ip_block['url']}")
    print(f"IP Prefix Address Family: {ip_block['family']['label']}")
    print()
