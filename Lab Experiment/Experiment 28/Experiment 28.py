import csv
from datetime import datetime

filename = input("Enter file activity log: ")

events = []

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Date"] + " " + row["Time"],
                "%Y-%m-%d %H:%M:%S"
            )

            events.append({
                "time": timestamp,
                "file": row["File"],
                "old_ext": row["OldExtension"],
                "new_ext": row["NewExtension"],
                "event": row["Event"]
            })

    events.sort(key=lambda x: x["time"])

    rapid_count = 0

    print("\nRansomware-Like Activity")
    print("--------------------------------")

    for i in range(1, len(events)):

        previous = events[i - 1]
        current = events[i]

        time_difference = (
            current["time"] - previous["time"]
        ).total_seconds()

        extension_changed = (
            current["old_ext"] != current["new_ext"]
        )

        if (
            current["event"].lower() == "modified"
            and time_difference <= 10
        ):

            rapid_count += 1

            print("[RAPID MODIFICATION]")
            print("Time :", current["time"])
            print("File :", current["file"])
            print()

        if extension_changed:

            print("[EXTENSION CHANGE]")
            print("File :", current["file"])
            print("Old Extension :", current["old_ext"])
            print("New Extension :", current["new_ext"])
            print()

    if rapid_count >= 2:
        print("WARNING: Ransomware-like activity detected!")

    elif rapid_count == 1:
        print("Suspicious rapid file modification detected.")

    else:
        print("No ransomware-like activity detected.")

except FileNotFoundError:
    print("File activity log does not exist.")
