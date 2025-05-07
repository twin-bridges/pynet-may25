"""
Create a Python script that contains a dictionary.

a. Using a try/except block, access a key in the dictionary that doesn't exist. Gracefully
   handle the exception in the "except KeyError:" block.

b. In this "except" block print a message stating "KeyError exception gracefully handled".

"""

routers = {
    "sf-rtr1": "192.168.1.1/24",
    "sf-rtr2": "192.168.1.2/24",
    "la-rtr1": "192.168.2.1/24",
    "la-rtr2": "192.168.2.2/24",
}

try:
    # Part a - try to access a key that doesn't exist.
    routers["missing_key"]
except KeyError:
    # Part b - gracefully handle the exception.
    print("KeyError exception gracefully handled")
