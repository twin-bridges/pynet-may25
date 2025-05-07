"""
Create a Python script that does the following:

a. Define a function named 'my_func' that uses three different parameters 'x', 'y', 'z'.
   Inside your function print out the value of each one of these parameters.

b. Call 'my_func' using entirely positional arguments.

c. Call 'my_func' using entirely named arguments.

d. Call 'my_func' using a mix of positional and named arguments. Remember positional
   arguments must be specified first.

"""


def my_func(x, y, z):
    print(f"{x = }")
    print(f"{y = }")
    print(f"{z = }")


# Call with positional arguments
print("\nFunc call: 'my_func(1, 2, 3)':")
my_func(1, 2, 3)

# Call with named arguments
print("\nFunc call: 'my_func(x=3, y=2, z=1)':")
my_func(x=3, y=2, z=1)

# Mixing positional and named arguments
print("\nFunc call: 'my_func(42, y=9, z=27)':")
my_func(42, y=9, z=27)
