import dns.resolver

domain = "nextinfosys.com.np"

try:
    answers = dns.resolver.resolve(domain, "A")
    for rdata in answers:
        print(rdata.to_text())
except dns.resolver.NXDOMAIN:
    print(f"{domain} does not exist.")
except dns.exception.DNSException as e:
    print("DNS error:", e)
