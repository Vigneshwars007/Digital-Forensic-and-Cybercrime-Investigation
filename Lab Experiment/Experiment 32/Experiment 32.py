import csv
from collections import Counter

filename = input("Enter network traffic log: ")

# Predefined suspicious destination IPs
suspicious_ips = [
    "203.0.113.25",
    "198.51.100.50",
    "10.10.10.50"
]

destination_count = Counter()

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        records = []

        for row in reader:

            source_ip = row["SourceIP"]
            destination_ip = row["DestinationIP"]

            # Store outbound traffic
            if row["Direction"].lower() == "outbound":

                records.append(row)
                destination_count[destination_ip] += 1

    print("\nUnusual Outbound Network Activity")
    print("--------------------------------")

    found = False

    for row in records:

        destination_ip = row["DestinationIP"]

        if destination_ip in suspicious_ips:

            print("\n[SUSPICIOUS OUTBOUND CONNECTION]")
            print("Date        :", row["Date"])
            print("Time        :", row["Time"])
            print("Source IP   :", row["SourceIP"])
            print("Destination :", row["DestinationIP"])
            print("Port        :", row["Port"])

            found = True

    print("\nRepeated Outbound Connections")
    print("--------------------------------")

    for ip, count in destination_count.items():

        if count >= 3:

            print(
                "[UNUSUAL]",
                ip,
                "-",
                count,
                "outbound connections"
            )

            found = True

    if not found:
        print("No unusual outbound activity detected.")

except FileNotFoundError:
    print("Network traffic log does not exist.")
