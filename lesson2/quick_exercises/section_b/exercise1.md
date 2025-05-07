
### a. Create a Python dictionary with the keys being data-center names ("sf1", "sf2", "la1", etc) and the values being fictional data center addresses.

```python
In [1]: data_centers = {
   ...:   "sf1": "200 Paul Ave",
   ...:   "sf2": "1 King Street",
   ...:   "sf3": "365 Main Street",
   ...:   "la1": "1 Wilshire Blvd.",
   ...: }
```

### b. Using '[key]' notation print out one of the values from the dictionary.

```python
In [2]: print(data_centers["la1"])
1 Wilshire Blvd.
```

### c. Using '[key]' notation add a new key-value pair to this data_centers dictionary.

```python
In [3]: data_centers["la2"] = "50 W. Hollywood Blvd."

In [4]: data_centers
Out[4]: 
{'sf1': '200 Paul Ave',
 'sf2': '1 King Street',
 'sf3': '365 Main Street',
 'la1': '1 Wilshire Blvd.',
 'la2': '50 W. Hollywood Blvd.'}
```

### d. Try to access a key that doesn't exist (i.e. a data-center name that is not in the dictionary) and observe the error that is generated.

```python
In [5]: data_centers["den1"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-5-a47e994eb924> in <module>
----> 1 data_centers["den1"]

KeyError: 'den1'
```

