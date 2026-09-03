import csv
from datetime import datetime

filename = input("Enter incident evidence log: ")

timeline = []

try:
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            timestamp = datetime.strptime(
                row["Date"] + " " + row["Time"],
                "%Y-%m-%d %H:%M:%S"
            )

            timeline.append(
                (
                    timestamp,
                    row["Source"],
                    row["Event"],
                    row["Details"]
                )
            )

    # Sort all events chronologically
    timeline.sort()

    print("\nIncident Response Timeline")
    print("--------------------------------")

    for timestamp, source, event, details in timeline:

        print(
            timestamp,
            "|",
            source,
            "|",
            event,
            "|",
            details
        )

except FileNotFoundError:
    print("Incident evidence log does not exist.")

except Exception as e:
    print("Error:", e)
