"""
Using the following NetBox URL:

url = "https://netbox.lasthop.io/api/dcim/sites/2/"

Retrieve the information regarding "Site 2" (Fremont Data Center). You should be able to
base this script on the following code:

request_get_w_auth.py

From the returned data structure print both the "name" and the "facility" fields.
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

    url = "https://netbox.lasthop.io/api/dcim/sites/2/"
    data = retrieve_url(url)
    name = data["name"]
    facility = data["facility"]

    print(f"\n{name=}")
    print(f"{facility=}\n")
