### Look at the data structure

```python
In [3]: data
Out[3]: 
{'nokia-conf:configure': {'card': [{'slot-number': 1,
    'mda': [{'mda-slot': 1, 'mda-type': 's36-100gb-qsfp28'}],
    'fp': [{'fp-number': 1}, {'fp-number': 2}]}]}}
```

### Determine it is a dictionary

```python
In [4]: type(data)
Out[4]: dict
```

### Look at the keys

```python
In [5]: data.keys()
Out[5]: dict_keys(['nokia-conf:configure'])
```

### Only a single key, drill into the data structure by looking at the value associated with that key.

```python
In [6]: conf = data['nokia-conf:configure']
```

### Look at new variable

```python
In [7]: conf
Out[7]: 
{'card': [{'slot-number': 1,
   'mda': [{'mda-slot': 1, 'mda-type': 's36-100gb-qsfp28'}],
   'fp': [{'fp-number': 1}, {'fp-number': 2}]}]}
```

### Determine it is a dictionary

```python
In [8]: type(conf)
Out[8]: dict
```

### Look at keys

```python
In [9]: conf.keys()
Out[9]: dict_keys(['card'])
```

### Only a single key, access value associated with that key.

```python
In [10]: modules = conf['card']
```

### Look at new variable

```python
In [11]: modules
Out[11]: 
[{'slot-number': 1,
  'mda': [{'mda-slot': 1, 'mda-type': 's36-100gb-qsfp28'}],
  'fp': [{'fp-number': 1}, {'fp-number': 2}]}]
```

### Determine that it is a list

```python
In [12]: type(modules)
Out[12]: list
```

### Look at the length of the list

```python
In [13]: len(modules)
Out[13]: 1
```

### Single element in the list, just access that element.

```python
In [13]: len(modules)
In [14]: modules = modules[0]
```

### Look at new variable; determine its type (dictionary)

```python
In [13]: len(modules)
In [15]: type(modules)
Out[15]: dict
```

### Look at the keys.

```python
In [16]: modules.keys()
Out[16]: dict_keys(['slot-number', 'mda', 'fp'])
```

### Now we can actually extract the data we want (slot_number)

```python
In [17]: slot_number = modules['slot-number']

In [18]: slot_number
Out[18]: 1
```

### Access 'mda' key and look at inner data structure

```python
In [19]: modules['mda']
Out[19]: [{'mda-slot': 1, 'mda-type': 's36-100gb-qsfp28'}]
```

### Inner data structure is single element list, so access that.

```python
In [20]: modules['mda'][0]
Out[20]: {'mda-slot': 1, 'mda-type': 's36-100gb-qsfp28'}
```

### Save this modules['mda'][0] as a new variable

```python
In [21]: slot_one = modules['mda'][0]

In [22]: slot_one
Out[22]: {'mda-slot': 1, 'mda-type': 's36-100gb-qsfp28'}
```

### Save the mda_slot_number as a variable.

```python
In [23]: mda_slot_number = slot_one['mda-slot']
```

### Save the mda_type as a variable

```python
In [24]: mda_type = slot_one['mda-type']
```

### Verify the mda variables

```python
In [25]: mda_slot_number
Out[25]: 1

In [26]: mda_type
Out[26]: 's36-100gb-qsfp28'
```
