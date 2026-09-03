import csv
from datetime import datetime


filename = input(
    "Enter ransomware investigation log file: "
)


records = []


# Predefined suspicious indicators
suspicious_keywords = [
    "malware",
    "unknown.exe",
    "powershell",
    "encrypted",
    ".locked",
    "failed login",
    "suspicious",
    "external connection"
]


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
                "event_type": row["EventType"],
                "details": row["Details"]
            })


    # Sort all events chronologically
    records.sort(
        key=lambda x: x["timestamp"]
    )


    print("\nRANSOMWARE INCIDENT ANALYSIS")
    print("========================================")


    # ----------------------------------------
    # Identify suspicious events
    # ----------------------------------------

    suspicious_events = []


    for record in records:

        details = record[
            "details"
        ].lower()

        event_type = record[
            "event_type"
        ].lower()


        combined_text = (
            event_type
            + " "
            + details
        )


        for keyword in suspicious_keywords:

            if keyword in combined_text:

                suspicious_events.append(
                    record
                )

                break


    # ----------------------------------------
    # Find probable starting point
    # ----------------------------------------

    if suspicious_events:

        starting_event = suspicious_events[0]


        print("\nPROBABLE INCIDENT STARTING POINT")
        print("----------------------------------------")

        print(
            "Timestamp:",
            starting_event["timestamp"]
        )

        print(
            "Event Type:",
            starting_event["event_type"]
        )

        print(
            "Details:",
            starting_event["details"]
        )


        # ----------------------------------------
        # Display subsequent suspicious activities
        # ----------------------------------------

        print(
            "\nSUBSEQUENT RELATED ACTIVITIES"
        )

        print("----------------------------------------")


        for event in suspicious_events:

            if (
                event["timestamp"]
                >= starting_event["timestamp"]
            ):

                print(
                    "\nTimestamp:",
                    event["timestamp"]
                )

                print(
                    "Event Type:",
                    event["event_type"]
                )

                print(
                    "Details:",
                    event["details"]
                )


    else:

        print(
            "\nNo suspicious events were detected."
        )


    # ----------------------------------------
    # Complete Timeline
    # ----------------------------------------

    print("\nCOMPLETE EVENT TIMELINE")
    print("========================================")


    for record in records:

        print(
            record["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "|",
            record["event_type"],
            "|",
            record["details"]
        )


except FileNotFoundError:

    print(
        "Investigation log file does not exist."
    )

except ValueError:

    print(
        "Invalid timestamp format in the log."
    )

except Exception as e:

    print("Error:", e)
