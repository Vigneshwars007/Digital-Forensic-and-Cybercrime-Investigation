import csv
from datetime import datetime


filename = input(
    "Enter malware activity log file: "
)


events = []


# Suspicious indicators
suspicious_names = [
    "malware.exe",
    "unknown.exe",
    "payload.exe",
    "ransom.exe"
]


unexpected_locations = [
    "Downloads",
    "Temp",
    "AppData"
]


persistence_keywords = [
    "startup",
    "registry run",
    "scheduled task",
    "persistence"
]


external_ip_prefixes = [
    "8.",
    "203.",
    "198."
]


try:

    # ----------------------------------------
    # Read Dataset
    # ----------------------------------------

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            events.append({
                "timestamp": timestamp,
                "event_type": row["EventType"],
                "process": row["Process"],
                "details": row["Details"]
            })


    print(
        "\nMALWARE TRIAGE ANALYSIS"
    )

    print(
        "========================================"
    )


    findings = []


    # ----------------------------------------
    # Analyze Events
    # ----------------------------------------

    for event in events:

        score = 0

        reasons = []


        process_name = event[
            "process"
        ].lower()


        details = event[
            "details"
        ].lower()


        event_type = event[
            "event_type"
        ].lower()


        # ------------------------------------
        # Suspicious Executable
        # ------------------------------------

        if process_name in suspicious_names:

            score += 30

            reasons.append(
                "Suspicious executable name"
            )


        # ------------------------------------
        # Unexpected File Location
        # ------------------------------------

        for location in unexpected_locations:

            if location.lower() in details:

                score += 20

                reasons.append(
                    "Executable running from "
                    "unexpected location: "
                    + location
                )

                break


        # ------------------------------------
        # Persistence Detection
        # ------------------------------------

        for keyword in persistence_keywords:

            if keyword in details:

                score += 30

                reasons.append(
                    "Possible persistence behavior: "
                    + keyword
                )

                break


        # ------------------------------------
        # Suspicious File-System Activity
        # ------------------------------------

        if event_type == "file":

            if (
                ".locked" in details
                or "encrypted" in details
                or "deleted security" in details
            ):

                score += 25

                reasons.append(
                    "Suspicious file-system activity"
                )


        # ------------------------------------
        # External Network Communication
        # ------------------------------------

        if event_type == "network":

            for prefix in external_ip_prefixes:

                if prefix in details:

                    score += 25

                    reasons.append(
                        "Possible external "
                        "network communication"
                    )

                    break


        # ------------------------------------
        # Store Suspicious Finding
        # ------------------------------------

        if score > 0:

            findings.append({
                "timestamp": event["timestamp"],
                "event_type": event["event_type"],
                "process": event["process"],
                "details": event["details"],
                "score": score,
                "reasons": reasons
            })


    # ----------------------------------------
    # Correlate Related Events
    # ----------------------------------------

    findings.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    print(
        "\nPRIORITIZED FINDINGS"
    )

    print(
        "========================================"
    )


    if findings:

        for finding in findings:

            print(
                "\n[PRIORITY SCORE:",
                finding["score"],
                "]"
            )


            print(
                "Timestamp:",
                finding["timestamp"]
            )


            print(
                "Event Type:",
                finding["event_type"]
            )


            print(
                "Process:",
                finding["process"]
            )


            print(
                "Details:",
                finding["details"]
            )


            print(
                "Reasons:"
            )


            for reason in finding["reasons"]:

                print(
                    "-",
                    reason
                )


            # Priority Classification

            if finding["score"] >= 60:

                print(
                    "Priority: HIGH"
                )

            elif finding["score"] >= 30:

                print(
                    "Priority: MEDIUM"
                )

            else:

                print(
                    "Priority: LOW"
                )


    else:

        print(
            "No suspicious events detected."
        )


    # ----------------------------------------
    # Timeline
    # ----------------------------------------

    print(
        "\nSUSPICIOUS EVENT TIMELINE"
    )

    print(
        "========================================"
    )


    findings.sort(
        key=lambda x: x["timestamp"]
    )


    for finding in findings:

        print(
            finding["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "|",
            finding["process"],
            "|",
            finding["event_type"]
        )


except FileNotFoundError:

    print(
        "Malware activity log file does not exist."
    )


except ValueError:

    print(
        "Invalid timestamp format."
    )


except Exception as e:

    print(
        "Error:",
        e
    )
