"""
Create a Python script that tries to access a variable that doesn't exist.

a. From running this program determine which exception type is generated and gracefully
   handle this exception. In the exception handler, just print("This variable does not
   exist.").

b. Add a "finally:" block after your exception handler and verify the finally block always
   executes (i.e. regardless of whether the exception occurs or not). Just print some message
   from this "finally:" block.

"""
try:
    # Comment / uncomment the 'var1' assigment line to test 'finally' block
    # var1 = "foo"
    # Try printing a variable that doesn't exit
    print(var1)
except NameError:
    print("This variable does not exist.")
finally:
    print("Always happens")
