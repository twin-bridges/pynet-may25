
### Given the following list of data centers:

```python
data_centers = ["sf1", "sf2", "la1", "la2", "den1", "dal1", "ny1", "ny2"]
```

### a. Create a new list using a list slice that consists of the four California data centers (i.e. the first four data centers).

```python
In [1]: data_centers = ["sf1", "sf2", "la1", "la2", "den1", "dal1", "ny1", "ny2"]

In [2]: ca_data_centers = data_centers[:4]

In [3]: ca_data_centers
Out[3]: ['sf1', 'sf2', 'la1', 'la2']
```

### b. Create a new list using a list slice that consists of the two New York data centers. The list slice should use at least one negative index in the slice.

```python
In [4]: ny_data_centers = data_centers[-2:]

In [5]: ny_data_centers
Out[5]: ['ny1', 'ny2']
```

