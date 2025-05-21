"""
Using an HTTP POST and the Python-requests library, create a new IP address object in
NetBox. This IP address object should be a /32 from the 203.0.113.0/24 documentation block.
Print out the status code and the returned JSON.

The HTTP headers for this request should look as follows:
http_headers = {}
http_headers["Content-Type"] = "application/json"
http_headers["accept"] = "application/json"
http_headers["Authorization"] = f"Token {token}"

The URL for the HTTP POST is:
https://netbox.lasthop.io/api/ipam/ip-addresses/

The JSON payload data for this request should be similar to the following:

# Where the last octet can be anywhere from .0 to .255
data = {"address": "203.0.113.0/32"}

"""
import os
import json
import requests
from rich import print

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"


def main():

    token = os.environ["NETBOX_TOKEN"]

    # HTTP POST needs the "Content-Type" header instead of "accept"
    http_headers = {}
    http_headers["Content-Type"] = "application/json"
    http_headers["accept"] = "application/json"
    http_headers["Authorization"] = f"Token {token}"

    # Required IP Address data
    data = {"address": "203.0.113.210/32"}

    # POST the data to Netbox
    # verify=False (self-signed SSL certificate) - this is insecure/not appropriate
    # for production use.
    resp = requests.post(
        f"{BASE_URL}ipam/ip-addresses/",
        headers=http_headers,
        verify=False,
        data=json.dumps(data),
    )

    # Response for Exercise 7a:
    print()
    print("Creating IP address object:")
    print(f"Response code: {resp.status_code}")
    print("Returned JSON:")
    print("-" * 12)
    print(resp.json())

    # Exercise 7b:
    # Retrieve the new object ID and query that specific object
    print()
    print("Query newly created object...")
    address_id = resp.json()["id"]

    # New URL specific to our new IP address object
    url = f"{BASE_URL}ipam/ip-addresses/{address_id}/"
    resp = requests.get(url, headers=http_headers, verify=False)
    print("-" * 12)
    print(resp.json())

    print()
    print(f"IP Addreses ID: {address_id}")
    print()


if __name__ == "__main__":
    main()
