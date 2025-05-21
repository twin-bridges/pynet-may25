### Inspect sys.path using 'python' REPL 
### Comments added by ktbyers

```python
>>> from rich import print
>>> import sys
>>> print(sys.path)
[
    '',     # Current working directory
    '/home/kbyers/python-libs', # From $PYTHONPATH
    '/home/kbyers/DJANGOX/djproject',   # From $PYTHONPATH
    '/usr/local/lib/python311.zip', # Compressed standard libraries
    '/usr/local/lib/python3.11',    # Standard libraries
    '/usr/local/lib/python3.11/lib-dynload',    # Standard libraries (c-extensions)
    '/home/kbyers/VENV/py3_venv/lib/python3.11/site-packages'   # VENV libraries
]
```
