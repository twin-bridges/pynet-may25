### In the lab environment type: 'env | grep PYTHONPATH' and inspect the current PYTHONPATH environment variable. 

Compare PYTHONPATH to the paths listed in sys.path from exercise5. Find the two directories in sys.path that are being set using PYTHONPATH.

```bash
$ env | grep PYTHONPATH
PYTHONPATH=/home/kbyers/python-libs:/home/kbyers/DJANGOX/djproject/
```

```python
>>> print(sys.path)
[
    '',
    '/home/kbyers/python-libs', # First directory in PYTHONPATH
    '/home/kbyers/DJANGOX/djproject', # Second directory in PYTHONPATH
    '/usr/local/lib/python311.zip',
    '/usr/local/lib/python3.11',
    '/usr/local/lib/python3.11/lib-dynload',
    '/home/kbyers/VENV/py3_venv/lib/python3.11/site-packages'
]
```
