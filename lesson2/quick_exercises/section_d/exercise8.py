"""

Create a Python script that reuses your function from exercise 2:

a. Call this function using positional arguments except use the *kwargs technique.

"""


# Function from Ex. 2
def my_func(x, y, z):
    print(f"{x = }")
    print(f"{y = }")
    print(f"{z = }")


# Key names MUST exactly match function parameters.
some_dict = {
    "x": "hello",
    "y": "world",
    "z": "something",
}

# Call with named arguments except using *kwargs
print("\nFunc call: 'my_func(**some_dict)':")
my_func(**some_dict)
