import re
from datetime import datetime


filename = input("Enter email header file: ")

records = []

try:

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:

        if line.startswith("Received:"):

            server_match = re.search(
                r"from\s+([^\s(]+)",
                line,
                re.IGNORECASE
            )

            ip_match = re.search(
                r"\[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]",
                line
            )

            timestamp_match = re.search(
                r";\s*(.+)$",
                line
            )

            server = (
                server_match.group(1)
                if server_match
                else "Unknown"
            )

            ip_address = (
                ip_match.group(1)
                if ip_match
                else "Unknown"
            )

            timestamp_text = (
                timestamp_match.group(1)
                if timestamp_match
                else "Unknown"
            )

            records.append({
                "server": server,
                "ip": ip_address,
                "timestamp": timestamp_text
            })


    print("\nEMAIL HEADER INVESTIGATION")
    print("================================")

    print("\nSIMPLIFIED MAIL DELIVERY PATH")
    print("--------------------------------")

    if not records:

        print("No Received headers found.")

    else:

        # Reverse order because Received headers
        # are commonly listed from newest to oldest
        delivery_path = list(reversed(records))

        for number, record in enumerate(
            delivery_path,
            start=1
        ):

            print("\nStep", number)
            print("Server    :", record["server"])
            print("IP Address:", record["ip"])
            print("Timestamp :", record["timestamp"])


        print("\nUNUSUAL ROUTING INFORMATION")
        print("--------------------------------")

        unusual_found = False

        for record in delivery_path:

            ip = record["ip"]

            if ip == "Unknown":

                print(
                    "[WARNING] IP address unavailable "
                    "for server:",
                    record["server"]
                )

                unusual_found = True

            elif (
                ip.startswith("10.")
                or ip.startswith("192.168.")
                or ip.startswith("172.16.")
            ):

                print(
                    "[NOTICE] Private IP address found:",
                    ip
                )

                print(
                    "Server:",
                    record["server"]
                )

                unusual_found = True


        if not unusual_found:

            print(
                "No predefined unusual routing "
                "information detected."
            )

except FileNotFoundError:

    print("Email header file does not exist.")

except Exception as e:

    print("Error:", e)
