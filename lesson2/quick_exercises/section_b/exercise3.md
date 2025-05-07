
### Using the Python REPL and the data_centers dictionary from exercise1:
### a. Use the .pop(key) method to delete a key from the dictionary. Print out the dictionary after you do this.

```python
In [6]: data_centers = {
   ...:     "sf1": "200 Paul Ave",
   ...:     "sf2": "1 King Street",
   ...:     "sf3": "365 Main Street",
   ...:     "la1": "1 Wilshire Blvd.",
   ...:     "la2": "50 W. Hollywood Blvd.",
   ...: }

In [7]: data_centers.pop("sf3")
Out[7]: '365 Main Street'

# Nicer printing...
In [9]: from rich import print

# "sf3" has been removed
In [10]: print(data_centers)
{
    'sf1': '200 Paul Ave',
    'sf2': '1 King Street',
    'la1': '1 Wilshire Blvd.',
    'la2': '50 W. Hollywood Blvd.'
}

```

### b. Use the 'del' operation to directly delete a second key from the dictionary. Print out the dictionary after you do this.

```python
In [11]: del data_centers["la2"]

# "la2" has been removed
In [12]: print(data_centers)
{'sf1': '200 Paul Ave', 'sf2': '1 King Street', 'la1': '1 Wilshire Blvd.'}
```

### c. Use the .update() method to re-add the two key-value pairs that you deleted. Print out the dictionary after you do this.

```python
# Define a new dictionary with 'sf3' and 'la2'
In [13]: new_dcs = {
    ...:   "sf3": "365 Main Street",
    ...:   'la2': '50 W. Hollywood Blvd.',
    ...: }

In [14]: print(new_dcs)
{'sf3': '365 Main Street', 'la2': '50 W. Hollywood Blvd.'}

In [15]: data_centers.update(new_dcs)

# 'sf3' and 'la2' are back in the data_centers dictionary (order of the keys has changed
# but that is fine.
In [16]: data_centers
Out[16]: 
{'sf1': '200 Paul Ave',
 'sf2': '1 King Street',
 'la1': '1 Wilshire Blvd.',
 'sf3': '365 Main Street',
 'la2': '50 W. Hollywood Blvd.'}
```

