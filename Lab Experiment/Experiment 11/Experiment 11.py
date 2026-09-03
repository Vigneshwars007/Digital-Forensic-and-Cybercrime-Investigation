from collections import defaultdict

threshold = 5
ports = defaultdict(set)

with open("network.log", "r", encoding="utf-8") as log:
    for line in log:
        parts = line.strip().split()
        if len(parts) == 2:
            src, port = parts
            ports[src].add(port)

print("Possible Port Scanners")
for ip, portset in ports.items():
    if len(portset) >= threshold:
        print(f"{ip} -> {len(portset)} unique ports scanned")
