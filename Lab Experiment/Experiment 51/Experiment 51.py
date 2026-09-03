import csv
from collections import defaultdict

filename = input("Enter network connection log: ")

records = []

HORIZONTAL_THRESHOLD = 3
VERTICAL_THRESHOLD = 3

try:

    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    print("\nNETWORK SCANNING ANALYSIS")
    print("================================")

    # ------------------------------------------
    # Horizontal Scan Detection
    # ------------------------------------------

    horizontal = defaultdict(list)

    for record in records:

        key = (
            record["SourceIP"],
            record["DestinationPort"]
        )

        horizontal[key].append(record)

    print("\nHORIZONTAL SCANNING")
    print("--------------------------------")

    horizontal_found = False

    for key, connections in horizontal.items():

        source_ip, port = key

        unique_hosts = set()

        for record in connections:
            unique_hosts.add(record["DestinationIP"])

        if len(unique_hosts) >= HORIZONTAL_THRESHOLD:

            print("\n[HORIZONTAL SCAN DETECTED]")
            print("Source IP       :", source_ip)
            print("Destination Port:", port)
            print("Hosts Contacted :", len(unique_hosts))

            print("\nSupporting Records:")

            for record in connections:

                print(
                    record["Timestamp"],
                    "|",
                    record["SourceIP"],
                    "->",
                    record["DestinationIP"],
                    ":",
                    record["DestinationPort"]
                )

            horizontal_found = True

    if not horizontal_found:
        print("No horizontal scanning detected.")

    # ------------------------------------------
    # Vertical Scan Detection
    # ------------------------------------------

    vertical = defaultdict(list)

    for record in records:

        key = (
            record["SourceIP"],
            record["DestinationIP"]
        )

        vertical[key].append(record)

    print("\nVERTICAL SCANNING")
    print("--------------------------------")

    vertical_found = False

    for key, connections in vertical.items():

        source_ip, destination_ip = key

        unique_ports = set()

        for record in connections:
            unique_ports.add(record["DestinationPort"])

        if len(unique_ports) >= VERTICAL_THRESHOLD:

            print("\n[VERTICAL SCAN DETECTED]")
            print("Source IP       :", source_ip)
            print("Destination Host:", destination_ip)
            print("Ports Contacted :", len(unique_ports))

            print("\nSupporting Records:")

            for record in connections:

                print(
                    record["Timestamp"],
                    "|",
                    record["SourceIP"],
                    "->",
                    record["DestinationIP"],
                    ":",
                    record["DestinationPort"]
                )

            vertical_found = True

    if not vertical_found:
        print("No vertical scanning detected.")

except FileNotFoundError:

    print("Network connection log does not exist.")

except Exception as e:

    print("Error:", e)
