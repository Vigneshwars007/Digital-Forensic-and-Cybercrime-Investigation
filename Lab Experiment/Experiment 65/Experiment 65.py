import csv
from datetime import datetime


timeline = []


def read_file_activity(filename):

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            timeline.append({
                "timestamp": timestamp,
                "source": "File Activity",
                "details":
                    row["FileName"]
                    + " - "
                    + row["Activity"]
            })


def read_authentication_log(filename):

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            timeline.append({
                "timestamp": timestamp,
                "source": "Authentication",
                "details":
                    "User: "
                    + row["User"]
                    + " | Status: "
                    + row["Status"]
            })


def read_browser_history(filename):

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            timeline.append({
                "timestamp": timestamp,
                "source": "Browser",
                "details":
                    row["URL"]
            })


def read_network_log(filename):

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            timeline.append({
                "timestamp": timestamp,
                "source": "Network",
                "details":
                    "Source: "
                    + row["SourceIP"]
                    + " -> Destination: "
                    + row["DestinationIP"]
            })


try:

    file_activity_file = input(
        "Enter file activity CSV file: "
    )

    authentication_file = input(
        "Enter authentication CSV file: "
    )

    browser_file = input(
        "Enter browser history CSV file: "
    )

    network_file = input(
        "Enter network log CSV file: "
    )


    read_file_activity(
        file_activity_file
    )

    read_authentication_log(
        authentication_file
    )

    read_browser_history(
        browser_file
    )

    read_network_log(
        network_file
    )


    # Sort all events chronologically

    timeline.sort(
        key=lambda x: x["timestamp"]
    )


    print("\nDIGITAL EVIDENCE TIMELINE")
    print("========================================")


    print("\nCOMPLETE CHRONOLOGICAL TIMELINE")
    print("----------------------------------------")


    for event in timeline:

        print(
            event["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "|",
            event["source"],
            "|",
            event["details"]
        )


    # Time interval for correlation

    correlation_seconds = 300


    print("\nCORRELATED EVENTS")
    print("----------------------------------------")

    print(
        "Events occurring within",
        correlation_seconds,
        "seconds:"
    )


    correlated_found = False


    for i in range(
        len(timeline) - 1
    ):

        current_event = timeline[i]

        next_event = timeline[i + 1]


        time_difference = (
            next_event["timestamp"]
            - current_event["timestamp"]
        ).total_seconds()


        if (
            time_difference
            <= correlation_seconds
            and current_event["source"]
            != next_event["source"]
        ):

            correlated_found = True


            print("\nPossible Correlation:")

            print(
                current_event["timestamp"],
                "|",
                current_event["source"],
                "|",
                current_event["details"]
            )

            print(
                next_event["timestamp"],
                "|",
                next_event["source"],
                "|",
                next_event["details"]
            )

            print(
                "Time Difference:",
                time_difference,
                "seconds"
            )


    if not correlated_found:

        print(
            "No closely related events found."
        )


except FileNotFoundError:

    print(
        "One or more log files do not exist."
    )

except ValueError:

    print(
        "Invalid timestamp format."
    )

except Exception as e:

    print("Error:", e)
