
### a. Create a tuple consisting of three IP addresses (strings)

```python
In [1]: ip_addresses = ("192.168.100.0/24", "172.16.1.0/24", "10.1.1.0/24")
```

### b. Print out the second IP address in the tuple.

```python
In [2]: print(ip_addresses[1])
172.16.1.0/24
```

### c. Attempt to modify the first IP address in the tuple (attempt to assign it using [0] notation)

```python
In [3]: ip_addresses[0] = "172.31.1.0/24"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[3], line 1
----> 1 ip_addresses[0] = "172.31.1.0/24"

TypeError: 'tuple' object does not support item assignment
```

