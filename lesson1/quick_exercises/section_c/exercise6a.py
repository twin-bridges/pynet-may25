# /usr/bin/env python
"""
a. Create a Python script that does the following:
   i. Prompts a use for an IP address.
   ii. Checks if the substring "192.168" exists in the IP address (don't worry about the
       location of this substring in the broader string i.e. this can occur in any pair of
       octets).
"""

ip_addr = input("Enter IP address: ")
check_ip = "192.168" in ip_addr

# 'check_ip' will print either True or False
print(f"\nIs '192.168' in the IP Address: {check_ip}")
