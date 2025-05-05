### a. In the REPL create the following:  `name = "Jerome Morrow"`

```python
In [10]: name = "Jerome Morrow"
```

### b. Use the .capitalize() method to convert the string to all upper case.

```python
In [12]: name.upper()
Out[12]: 'JEROME MORROW'
```

### c. Create a new name variable: `name = "  Jerome Morrow\n\t "`. This `name` variable contains whitespace both before and after the name. Call the .strip() method on this variable and verify that all the whitespace before and after the name was removed.

```python
In [13]: name = " Jerome Morrow\n\t "

In [14]: name
Out[14]: ' Jerome Morrow\n\t '

In [15]: name.strip()
Out[15]: 'Jerome Morrow'
```

