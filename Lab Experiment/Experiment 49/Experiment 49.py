import csv
from collections import defaultdict
from datetime import datetime

filename = input("Enter authentication log: ")

records = []

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Date"] + " " + row["Time"],
                "%Y-%m-%d %H:%M:%S"
            )

            row["Timestamp"] = timestamp

            records.append(row)

    # Sort records chronologically
    records.sort(key=lambda x: x["Timestamp"])

    print("\nAUTHENTICATION FORENSIC ANALYSIS")
    print("================================")

    # ------------------------------------------------
    # Finding 1: Failures followed by successful login
    # ------------------------------------------------

    print("\nFINDING 1: FAILURES FOLLOWED BY SUCCESS")
    print("--------------------------------")

    finding_1 = False

    for i in range(1, len(records)):

        previous = records[i - 1]
        current = records[i]

        if (
            previous["Status"].lower() == "failed"
            and current["Status"].lower() == "success"
            and previous["Username"] == current["Username"]
            and previous["SourceIP"] == current["SourceIP"]
        ):

            print(
                "[SUSPICIOUS SEQUENCE]"
            )

            print(
                "Failed:",
                previous["Timestamp"],
                "| User:",
                previous["Username"],
                "| IP:",
                previous["SourceIP"]
            )

            print(
                "Success:",
                current["Timestamp"],
                "| User:",
                current["Username"],
                "| IP:",
                current["SourceIP"]
            )

            finding_1 = True

    if not finding_1:
        print("No failure-to-success sequence detected.")

    # ------------------------------------------------
    # Finding 2: One IP targeting multiple accounts
    # ------------------------------------------------

    print("\nFINDING 2: MULTIPLE-ACCOUNT TARGETING")
    print("--------------------------------")

    ip_accounts = defaultdict(set)

    for record in records:

        if record["Status"].lower() == "failed":

            ip_accounts[
                record["SourceIP"]
            ].add(
                record["Username"]
            )

    finding_2 = False

    for ip, accounts in ip_accounts.items():

        if len(accounts) >= 3:

            print(
                "[MULTIPLE ACCOUNT TARGETING]"
            )

            print("Source IP:", ip)
            print("Accounts:", ", ".join(accounts))
            print(
                "Number of Accounts:",
                len(accounts)
            )

            finding_2 = True

    if not finding_2:
        print("No multiple-account targeting detected.")

    # ------------------------------------------------
    # Finding 3: Concentrated attempts against account
    # ------------------------------------------------

    print("\nFINDING 3: SINGLE-ACCOUNT TARGETING")
    print("--------------------------------")

    account_failures = defaultdict(list)

    for record in records:

        if record["Status"].lower() == "failed":

            key = (
                record["Username"],
                record["SourceIP"]
            )

            account_failures[key].append(record)

    finding_3 = False

    for (username, ip), attempts in account_failures.items():

        if len(attempts) >= 3:

            print(
                "[CONCENTRATED ATTACK PATTERN]"
            )

            print("Username:", username)
            print("Source IP:", ip)
            print(
                "Failed Attempts:",
                len(attempts)
            )

            print("Supporting Records:")

            for record in attempts:

                print(
                    " -",
                    record["Timestamp"],
                    "|",
                    record["Status"]
                )

            finding_3 = True

    if not finding_3:
        print("No concentrated account targeting detected.")

except FileNotFoundError:

    print("Authentication log does not exist.")

except Exception as e:

    print("Error:", e)
