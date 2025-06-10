import django

django.setup()

from net_db.models import NetworkDevice  # noqa
from net_db.models import Interface  # noqa

cisco3 = NetworkDevice(
    name="cisco3", host="cisco3.lasthop.io", device_type="cisco_ios", username="pyclass"
)
cisco3.save()

gi0_0_0 = Interface(
    device=cisco3, intf_name="GigabitEthernet0/0/0", intf_type="1000BaseT"
)
gi0_0_0.save()

print(cisco3)
print(gi0_0_0)
