"""
Create a Python script using "pathlib".

This script should create a Path object corresponding to "~/ntc-templates" (in other words,
corresponding to your home directory and the ntc-templates subdirectory).

From this ntc-templates subdirectory, you should use the following globstar pattern to find
all of the "*.textfsm" templates inside of this subdirectory.

for child in ntc_templates.glob("**/*.textfsm"):
    print(child)

Print out all of the "*.textfsm" files that you find (there will be a lot of them, on the order of
900).

Repeat this globstar search and see if you can find any "ciena" templates (note, "ciena" will
be all lower case in the template names).

"""
from pathlib import Path
from rich import print

home = Path.home()
ntc_templates = home / "ntc-templates"

# Print out all of the files ending in .textfsm
print("\nAll .textfsm templates: ")
print("#" * 50)
for child in ntc_templates.glob("**/*.textfsm"):
    print(child)
print("#" * 50)

# Note, you could also find all of the .textfsm templates and then
# add a conditional to look only for the 'ciena' templates (inside the for loop).
print("\nOnly 'ciena' .textfsm templates: ")
print("#" * 50)
for ciena_child in ntc_templates.glob("**/*ciena*.textfsm"):
    print(ciena_child)
print("#" * 50)
print()
