
### a. Using the REPL, create a variable named 'my_address' and assign it to be a string.

```
$ python -m IPython
Python 3.12.0 (main, Oct  4 2023, 19:22:22) [GCC 11.4.1 20230605 (Red Hat 11.4.1-2)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: my_address = "10 Elm Street"
```


### b. In the REPL, execute 'dir(my_address)' and look at the string methods available to you.

```python
In [2]: dir(my_address)
Out[2]: 
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 # A bunch more methods.
```


### c. In the REPL, execute 'help(my_address.strip)' and look at the help for the 'strip()' string method.

```
In [3]: help(my_address.strip)
------------
Help on built-in function strip:

strip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading and trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead.
------------
```

