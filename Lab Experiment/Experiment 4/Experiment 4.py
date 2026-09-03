import socket

with open("domain.txt", "r", encoding="utf-8") as file:
    domain = file.read().strip()

try:
    ip = socket.gethostbyname(domain)
    print("DNS Lookup Successful")
    print("Domain     :", domain)
    print("IP Address :", ip)
except socket.gaierror:
    print("DNS Lookup Failed for:", domain)
