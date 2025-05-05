
### a. Which of the following are valid Python variable names: some_var, _, Some_Var9, 9_A_VAR, var99?

```
$ python
Python 3.12.0 (main, Oct  4 2023, 19:22:22) [GCC 11.4.1 20230605 (Red Hat 11.4.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> some_var = "hello"
>>> _ = "hello"
>>> Some_Var9 = "hello"
>>> 9_A_VAR = "hello"  # invalid
  File "<stdin>", line 1
    9_A_VAR = "hello"  # invalid
     ^
SyntaxError: invalid decimal literal
>>> var99 = "hello"
```

```
Answer: 
    Invalid: 9_A_VAR

    All other variable names are valid names.
```


### b. What is the meaning of a variable that starts with a single leading underscore like: _special_var?

   Leading underscore before variable names: means "private" (private variable, attribute, 
   method.


### c. What is the name/meaning of variables that start and end with double underscore like: __name__?

   Dunder variables or magic methods are basically special variables or methods in Python 
   that have internal special meaning to Python. 

   For example, __init__ in a "class" context is the special method that gets automatically 
   called to initialize an object.

   Or as a second example, __str__ in a class context is a method that is automatically used
   when someone tries to print() the given object (i.e. the informal string representation
   of an object).


### d. Make sure you can execute python and enter the Python REPL (typically this is either via typing "python3" or by typing "python3 -m IPython

```
$ python3 -m IPython
Python 3.12.0 (main, Oct  4 2023, 19:22:22) [GCC 11.4.1 20230605 (Red Hat 11.4.1-2)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: quit()
```

```
$ python
Python 3.12.0 (main, Oct  4 2023, 19:22:22) [GCC 11.4.1 20230605 (Red Hat 11.4.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```
   
