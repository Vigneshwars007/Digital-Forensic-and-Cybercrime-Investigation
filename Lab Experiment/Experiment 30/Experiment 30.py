import csv

filename = input("Enter network security log: ")

# Predefined threat indicator IP addresses
threat_ips = [
    "192.168.1.100",
    "10.10.10.50",
    "203.0.113.25"
]

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\nSuspicious IP Addresses")
        print("--------------------------------")

        found = False

        for row in reader:

            source_ip = row["SourceIP"]

            if source_ip in threat_ips:

                print("\n[SUSPICIOUS IP]")
                print("Date       :", row["Date"])
                print("Time       :", row["Time"])
                print("Source IP  :", row["SourceIP"])
                print("Destination:", row["DestinationIP"])
                print("Port       :", row["Port"])
                print("Status     :", row["Status"])

                found = True

        if not found:
            print("No suspicious IP addresses found.")

except FileNotFoundError:
    print("Network security log does not exist.")
