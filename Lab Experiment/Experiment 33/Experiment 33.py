import csv
from collections import Counter

filename = input("Enter packet log file: ")

packet_count = Counter()

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        records = []

        for row in reader:

            source_ip = row["SourceIP"]

            packet_count[source_ip] += 1
            records.append(row)

    print("\nPacket Analysis")
    print("--------------------------------")

    for ip, count in packet_count.items():

        print(
            "Source IP:",
            ip,
            "| Packets:",
            count
        )

    print("\nPossible DoS Attack Patterns")
    print("--------------------------------")

    found = False

    # Threshold for this simulated experiment
    threshold = 5

    for ip, count in packet_count.items():

        if count >= threshold:

            print(
                "[POSSIBLE DOS]",
                ip,
                "-",
                count,
                "packets"
            )

            found = True

    if not found:
        print("No possible DoS attack pattern detected.")

except FileNotFoundError:
    print("Packet log file does not exist.")
