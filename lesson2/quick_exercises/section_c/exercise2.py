"""
In a Python script create the following two data-structures:

ip_addresses = ["192.168.0.0/24", "192.168.1.0/24", "192.168.2.0/24", "192.168.3.0/24"]
routers = {
    "sf-rtr1": "192.168.1.1/24",
    "sf-rtr2": "192.168.1.2/24",
    "la-rtr1": "192.168.2.1/24",
    "la-rtr2": "192.168.2.2/24",
}

Now create a try/except block that handles both a "KeyError" exception and an "IndexError"
exception. In the case of a "KeyError" print a message stating, "'KeyError' exception handler".
In the case of an IndexError print a message stating, "'IndexError' exception handler".

Test your code properly handles both error cases.

"""

ip_addresses = ["192.168.0.0/24", "192.168.1.0/24", "192.168.2.0/24", "192.168.3.0/24"]
routers = {
    "sf-rtr1": "192.168.1.1/24",
    "sf-rtr2": "192.168.1.2/24",
    "la-rtr1": "192.168.2.1/24",
    "la-rtr2": "192.168.2.2/24",
}

try:
    # Only the first exception will actually happen (so swap order to test both cases).
    print("\nInside 'try' block")
    ip_addresses[10]
    routers["invalid"]
except KeyError:
    print("'KeyError' exception handler")
except IndexError:
    print("'IndexError' exception handler")

print("After try/except block\n")
