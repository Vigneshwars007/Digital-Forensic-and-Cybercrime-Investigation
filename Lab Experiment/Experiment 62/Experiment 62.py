import csv
from datetime import datetime
from collections import defaultdict


filename = input("Enter authentication log file: ")

records = []

FAILURE_THRESHOLD = 3
UNUSUAL_START_HOUR = 0
UNUSUAL_END_HOUR = 5


try:

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            records.append({
                "timestamp": timestamp,
                "user": row["User"],
                "source_ip": row["SourceIP"],
                "status": row["Status"]
            })


    records.sort(
        key=lambda x: x["timestamp"]
    )


    print("\nAUTHENTICATION EVENT LOG ANALYSIS")
    print("========================================")


    # ----------------------------------------
    # 1. Failed Logins Followed by Success
    # ----------------------------------------

    print("\n1. SUCCESSFUL LOGIN AFTER FAILURES")
    print("----------------------------------------")

    failed_attempts = defaultdict(list)

    finding_found = False


    for record in records:

        user = record["user"]

        if record["status"].lower() == "failure":

            failed_attempts[user].append(record)

        elif record["status"].lower() == "success":

            if len(failed_attempts[user]) >= FAILURE_THRESHOLD:

                finding_found = True

                print(
                    "\n[ALERT] Successful login after",
                    len(failed_attempts[user]),
                    "failures"
                )

                print("User:", user)

                print("\nFailed Login Records:")

                for failure in failed_attempts[user]:

                    print(
                        failure["timestamp"],
                        "|",
                        failure["source_ip"],
                        "| FAILURE"
                    )

                print("\nSuccessful Login:")

                print(
                    record["timestamp"],
                    "|",
                    record["source_ip"],
                    "| SUCCESS"
                )

            failed_attempts[user] = []


    if not finding_found:

        print(
            "No successful logins after repeated "
            "failures detected."
        )


    # ----------------------------------------
    # 2. Authentication at Unusual Times
    # ----------------------------------------

    print("\n2. UNUSUAL LOGIN TIMES")
    print("----------------------------------------")

    unusual_found = False


    for record in records:

        hour = record["timestamp"].hour

        if (
            UNUSUAL_START_HOUR
            <= hour
            <= UNUSUAL_END_HOUR
        ):

            unusual_found = True

            print(
                "\n[UNUSUAL TIME]"
            )

            print(
                "Time:",
                record["timestamp"]
            )

            print(
                "User:",
                record["user"]
            )

            print(
                "Source IP:",
                record["source_ip"]
            )

            print(
                "Status:",
                record["status"]
            )


    if not unusual_found:

        print(
            "No unusual-time authentication "
            "activity detected."
        )


    # ----------------------------------------
    # 3. New Source Address Detection
    # ----------------------------------------

    print("\n3. NEW SOURCE ADDRESS ACTIVITY")
    print("----------------------------------------")

    known_sources = defaultdict(set)

    new_source_found = False


    for record in records:

        user = record["user"]
        source_ip = record["source_ip"]

        if source_ip not in known_sources[user]:

            if len(known_sources[user]) > 0:

                new_source_found = True

                print(
                    "\n[NEW SOURCE ADDRESS]"
                )

                print(
                    "User:",
                    user
                )

                print(
                    "New Source IP:",
                    source_ip
                )

                print(
                    "Timestamp:",
                    record["timestamp"]
                )

                print(
                    "Status:",
                    record["status"]
                )

            known_sources[user].add(
                source_ip
            )


    if not new_source_found:

        print(
            "No new source addresses detected."
        )


except FileNotFoundError:

    print(
        "Authentication log file does not exist."
    )

except ValueError:

    print(
        "Invalid timestamp format in the log."
    )

except Exception as e:

    print("Error:", e)
