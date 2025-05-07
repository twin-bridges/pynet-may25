"""
Create a Python script that does the following:
a. Contains a simple function with no parameters that executes three print statements and
   returns 42

b. Call this function three times and verify your code executes properly.

"""


# Part a.
def my_func():
    print("Hello")
    print("World")
    print("And Something Else.\n")
    return 42


# Part b. (actually call the function three times)
my_func()
my_func()
# Save the return value(42) in this last call (don't do anything with it).
ret_val = my_func()
