from django.db import models


class NetworkDevice(models.Model):
    name = models.CharField(max_length=30)
    host = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Interface(models.Model):
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, related_name="interfaces"
    )
    intf_name = models.CharField(max_length=100)
    intf_type = models.CharField(max_length=100)

    def __str__(self):
        return self.intf_name


class DNSServer(models.Model):
    ip_addr = models.GenericIPAddressField(primary_key=True)
    hostname = models.CharField(max_length=255)
    provider = models.CharField(max_length=50)
