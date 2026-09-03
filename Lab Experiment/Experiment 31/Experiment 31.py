import csv
from collections import Counter

filename = input("Enter firewall log file: ")

blocked_ips = Counter()

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\nBlocked Firewall Connections")
        print("--------------------------------")

        for row in reader:

            if row["Status"].lower() == "blocked":

                source_ip = row["SourceIP"]

                blocked_ips[source_ip] += 1

                print(
                    row["Date"],
                    row["Time"],
                    "| Source IP:",
                    source_ip,
                    "| Destination:",
                    row["DestinationIP"],
                    "| Port:",
                    row["Port"]
                )

        print("\nRepeated Unauthorized Access Attempts")
        print("--------------------------------")

        found = False

        for ip, count in blocked_ips.items():

            if count >= 3:

                print(
                    "[SUSPICIOUS]",
                    ip,
                    "-",
                    count,
                    "blocked attempts"
                )

                found = True

        if not found:
            print("No repeated unauthorized access attempts found.")

except FileNotFoundError:
    print("Firewall log file does not exist.")
