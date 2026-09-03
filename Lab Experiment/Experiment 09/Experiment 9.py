from collections import Counter

threshold = 3
failed = Counter()

with open("login.log", "r", encoding="utf-8") as log:
    for line in log:
        parts = line.strip().split()
        if "FAILED" in parts:
            ip = parts[-1]
            failed[ip] += 1

print("Suspicious IP Addresses")
for ip, count in failed.items():
    if count >= threshold:
        print(f"{ip} -> {count} failed attempts")
