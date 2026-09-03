import socket
from collections import defaultdict

filename = input("Enter domain list file: ")

domain_ips = {}
ip_domains = defaultdict(list)
failed_domains = []

try:
    with open(filename, "r") as file:

        domains = [
            line.strip()
            for line in file
            if line.strip()
        ]

    for domain in domains:

        try:
            ip_address = socket.gethostbyname(domain)

            domain_ips[domain] = ip_address
            ip_domains[ip_address].append(domain)

        except socket.gaierror:
            failed_domains.append(domain)

    print("\nDNS RECONNAISSANCE SUMMARY")
    print("--------------------------------")

    print("\nResolved Domains")
    print("--------------------------------")

    for domain, ip in domain_ips.items():
        print(domain, "->", ip)

    print("\nDomains Sharing Same IP")
    print("--------------------------------")

    found_shared = False

    for ip, domains in ip_domains.items():

        if len(domains) > 1:

            print("\nIP Address:", ip)

            for domain in domains:
                print(" -", domain)

            found_shared = True

    if not found_shared:
        print("No domains sharing the same IP were found.")

    print("\nDNS Resolution Failures")
    print("--------------------------------")

    if failed_domains:

        for domain in failed_domains:
            print("[FAILED] :", domain)

    else:
        print("No DNS resolution failures.")

except FileNotFoundError:
    print("Domain list file does not exist.")
