import csv
from collections import defaultdict

filename = input("Enter network connection log file: ")

HORIZONTAL_THRESHOLD = 3
VERTICAL_THRESHOLD = 3

records = []

try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    # Horizontal scanning analysis
    horizontal = defaultdict(list)

    for record in records:
        key = (
            record["SourceIP"],
            record["DestinationPort"]
        )

        horizontal[key].append(record)

    print("\nHORIZONTAL SCANNING")
    print("-------------------------")

    found = False

    for key, connections in horizontal.items():

        source_ip, port = key

        hosts = set()

        for record in connections:
            hosts.add(record["DestinationIP"])

        if len(hosts) >= HORIZONTAL_THRESHOLD:

            print("\nHorizontal Scan Detected")
            print("Source IP:", source_ip)
            print("Port:", port)
            print("Hosts Contacted:", len(hosts))

            for record in connections:
                print(record)

            found = True

    if not found:
        print("No horizontal scanning detected.")

    # Vertical scanning analysis
    vertical = defaultdict(list)

    for record in records:

        key = (
            record["SourceIP"],
            record["DestinationIP"]
        )

        vertical[key].append(record)

    print("\nVERTICAL SCANNING")
    print("-------------------------")

    found = False

    for key, connections in vertical.items():

        source_ip, destination_ip = key

        ports = set()

        for record in connections:
            ports.add(record["DestinationPort"])

        if len(ports) >= VERTICAL_THRESHOLD:

            print("\nVertical Scan Detected")
            print("Source IP:", source_ip)
            print("Destination IP:", destination_ip)
            print("Ports Contacted:", len(ports))

            for record in connections:
                print(record)

            found = True

    if not found:
        print("No vertical scanning detected.")

except FileNotFoundError:
    print("File not found.")
