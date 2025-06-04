from pathlib import Path
from rich import print

home = Path.home()
ntc_templates = home / "ntc-templates"

for child in ntc_templates.glob("**/*.textfsm"):
    if "juniper_junos_show_bgp_summary" in child.name:
        juniper_show_bgp = child

with open(juniper_show_bgp) as f:
    juniper_template = f.read()

print(juniper_template)
