### a. Creates a list of five different first names.

```python
In [5]: names = ["George", "John", "Thomas", "James", "Andrew"]
```

### b. Use the .append() method twice to add two names to this list. Print the list to verify the new names are now included in the list.

```python
In [6]: names.append("Martin")

In [7]: names.append("William")
In [8]: names

Out[8]: ['George', 'John', 'Thomas', 'James', 'Andrew', 'Martin', 'William']
```

### c. Use the .pop() method to pop() the last name off the list. Save this value in a variable named 'new_name'.

```python
In [9]: new_name = names.pop()

# I verified this slightly later
In [12]: new_name
Out[12]: 'William'
```

### d. Use the .pop(0) method to pop() the very first name off the list. Save this value in a variable named 'other_name'.

```python
In [10]: other_name = names.pop(0)

# I verified this slightly later
In [13]: other_name
Out[13]: 'George'
```

### e. Print out the list after the two pop() operations and verify the list contents. Verify that the list changed in the way you expected.

```python
# Before .pop() operations, the list contained the following:
Out[8]: ['George', 'John', 'Thomas', 'James', 'Andrew', 'Martin', 'William']

In [11]: names
Out[11]: ['John', 'Thomas', 'James', 'Andrew', 'Martin']
```

Explanation, we popped the last name off the list (i.e. "William") and then we popped the
first name off the list (i.e. "George").

