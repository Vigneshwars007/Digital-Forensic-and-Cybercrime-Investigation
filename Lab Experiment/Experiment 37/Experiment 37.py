import csv
from collections import Counter

filename = input("Enter authentication log: ")

user_failures = Counter()
ip_failures = Counter()

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Status"].lower() == "failed":

                username = row["Username"]
                source_ip = row["SourceIP"]

                user_failures[username] += 1
                ip_failures[source_ip] += 1

    print("\nAuthentication Failure Analysis")
    print("--------------------------------")

    print("\nFailed Attempts by User")

    for user, count in user_failures.items():
        print(user, ":", count, "failed attempts")

    print("\nFailed Attempts by IP Address")

    for ip, count in ip_failures.items():
        print(ip, ":", count, "failed attempts")

    print("\nPossible Password Attack Patterns")
    print("--------------------------------")

    threshold = 3
    found = False

    for user, count in user_failures.items():

        if count >= threshold:

            print(
                "[SUSPICIOUS USER]",
                user,
                "-",
                count,
                "failed attempts"
            )

            found = True

    for ip, count in ip_failures.items():

        if count >= threshold:

            print(
                "[SUSPICIOUS IP]",
                ip,
                "-",
                count,
                "failed attempts"
            )

            found = True

    if not found:
        print("No possible password attack detected.")

except FileNotFoundError:
    print("Authentication log does not exist.")
