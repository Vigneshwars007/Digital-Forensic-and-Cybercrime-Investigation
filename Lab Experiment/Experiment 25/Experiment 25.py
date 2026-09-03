import csv
from datetime import datetime

file_log = input("Enter file timestamp log: ")
system_log = input("Enter system log: ")

timeline = []

try:
    # Read file timestamp records
    with open(file_log, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Date"] + " " + row["Time"],
                "%Y-%m-%d %H:%M:%S"
            )

            timeline.append(
                (
                    timestamp,
                    "FILE",
                    row["Event"],
                    row["File"]
                )
            )

    # Read system log records
    with open(system_log, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Date"] + " " + row["Time"],
                "%Y-%m-%d %H:%M:%S"
            )

            timeline.append(
                (
                    timestamp,
                    "SYSTEM",
                    row["Event"],
                    row["Details"]
                )
            )

    # Sort events by date and time
    timeline.sort()

    print("\nDigital Event Timeline")
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
    print("Log file does not exist.")

except Exception as e:
    print("Error:", e)
