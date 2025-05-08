"""

Create a Python script that reuses your function from exercise 2:

a. Call this function using positional arguments except use the *args technique.

"""


# Function from Ex. 2
def my_func(x, y, z):
    print(f"{x = }")
    print(f"{y = }")
    print(f"{z = }")


my_args = [7, 8, 42]

# Call with positional arguments except using *args technique
print("\nFunc call: 'my_func(*my_args)':")
my_func(*my_args)

# Also works if my_args is a tuple:
my_args = (7, 8, 99)
print("\nFunc call: 'my_func(*my_args)': (tuple)")
my_func(*my_args)
