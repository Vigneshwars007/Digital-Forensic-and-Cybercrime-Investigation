import csv
from datetime import datetime

filename = input("Enter activity log file: ")

records = []

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            time_value = datetime.strptime(
                row["Date"] + " " + row["Time"],
                "%Y-%m-%d %H:%M:%S"
            )

            records.append(
                (time_value, row["User"], row["File"])
            )

    # Sort records from newest to oldest
    records.sort(reverse=True)

    print("\nRecently Accessed Files")
    print("-----------------------------")

    for time_value, user, file_name in records:
        print("Time :", time_value)
        print("User :", user)
        print("File :", file_name)
        print()

except FileNotFoundError:
    print("Activity log file does not exist.")

except Exception as e:
    print("Error:", e)
