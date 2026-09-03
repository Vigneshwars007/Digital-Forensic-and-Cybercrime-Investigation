import csv
from collections import Counter

filename = input("Enter Windows event log file: ")

failed_users = Counter()

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Status"].lower() == "failed":
                failed_users[row["Username"]] += 1

    print("\nFailed Login Attempts")
    print("-----------------------------")

    for user, count in failed_users.items():
        print(user, ":", count, "failed attempts")

    print("\nRepeated Failed Login Attempts")
    print("-----------------------------")

    found = False

    for user, count in failed_users.items():

        if count >= 3:
            print(
                "[SUSPICIOUS] User:",
                user,
                "-",
                count,
                "failed attempts"
            )
            found = True

    if not found:
        print("No repeated failed login attempts found.")

except FileNotFoundError:
    print("Windows event log file does not exist.")
