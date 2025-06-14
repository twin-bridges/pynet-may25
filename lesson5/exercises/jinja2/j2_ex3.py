from jinja2 import FileSystemLoader, StrictUndefined
from jinja2 import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

local_bgp_defs = {
    "bgp_as": 65000,
    "bgp_router_id": "1.1.1.1",
}
cust1_ref_id = "cust422"
customer_bgp_defs = {
    "customer_reference": cust1_ref_id,
    "customer_bgp_peer_group": f"{cust1_ref_id.upper()}-PEER-GROUP",
    "customer_bgp_afi_ipv4": True,
    "customer_bgp_afi_ipv6": True,
    "customer_bgp_as": 64999,
    "customer_bgp_neighbors": ["172.31.254.1", "172.31.7.1"],
}
j2_vars = local_bgp_defs
j2_vars.update(customer_bgp_defs)

template_file = "sros_bgp_ex3.j2"
template = env.get_template(template_file)
output = template.render(**j2_vars)
print(output)
