import csv
from datetime import datetime

filename = input("Enter ransomware incident log: ")

events = []

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Date"] + " " + row["Time"],
                "%Y-%m-%d %H:%M:%S"
            )

            events.append(
                (
                    timestamp,
                    row["Event"],
                    row["Details"]
                )
            )

    # Sort events chronologically
    events.sort()

    print("\nRansomware Attack Timeline")
    print("--------------------------------")

    for timestamp, event, details in events:

        print(
            timestamp,
            "|",
            event,
            "|",
            details
        )

except FileNotFoundError:
    print("Ransomware incident log does not exist.")

except Exception as e:
    print("Error:", e)
