import django

django.setup()

from net_db.models import DNSServer  # noqa

cf1 = DNSServer(ip_addr="1.1.1.1", hostname="one.one.one.one", provider="Cloudflare")
cf1.save()

cf2 = DNSServer(ip_addr="1.0.0.1", hostname="one.one.one.one", provider="Cloudflare")
cf2.save()

google1 = DNSServer(ip_addr="8.8.8.8", hostname="dns.google", provider="Google")
google1.save()

google2 = DNSServer(ip_addr="8.4.4.8", hostname="dns.google", provider="Google")
google2.save()

dns_servers = DNSServer.objects.all()
print(dns_servers)
