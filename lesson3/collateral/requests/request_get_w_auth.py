import os
import requests
from rich import print


from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    # url = "https://netbox.lasthop.io/api/dcim/devices/"
    url = "https://netbox.lasthop.io/api/dcim/devices/1/"
    http_headers = {"accept": "application/json"}
    if token:
        http_headers["authorization"] = "Token {}".format(token)

    # verify=False (self-signed SSL certificate) - this is insecure/not appropriate
    # for production use.
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

    print()
    print(response)
    print()
