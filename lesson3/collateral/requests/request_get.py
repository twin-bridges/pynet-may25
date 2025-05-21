import requests
from rich import print

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    # Failed auth
    # url = "https://netbox.lasthop.io/api/dcim/devices/"
    # Working no auth
    url = "https://netbox.lasthop.io/api/dcim/"
    # url = "https://api.github.com/"
    http_headers = {"accept": "application/json"}

    # verify=False (self-signed SSL certificate) - this is insecure/not appropriate
    # for production use.
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

    print()
    print(response)
    print()
