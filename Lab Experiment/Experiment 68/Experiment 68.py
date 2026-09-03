import csv
import os
from datetime import datetime
from collections import Counter


filename = input(
    "Enter file renaming log file: "
)

records = []


# Threshold values
FILE_THRESHOLD = 5
RAPID_INTERVAL = 60


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
                "original": row["OriginalFile"],
                "renamed": row["RenamedFile"],
                "directory": row["Directory"]
            })


    # Sort events chronologically
    records.sort(
        key=lambda x: x["timestamp"]
    )


    print("\nRANSOMWARE ACTIVITY ANALYSIS")
    print("========================================")


    total_files = len(records)

    risk_score = 0


    # ----------------------------------------
    # 1. Number of Files Affected
    # ----------------------------------------

    print("\n1. FILES AFFECTED")
    print("----------------------------------------")

    print(
        "Total Renaming Events:",
        total_files
    )


    if total_files >= FILE_THRESHOLD:

        risk_score += 30

        print(
            "[WARNING] Large number of files "
            "affected."
        )

    else:

        print(
            "Number of affected files is low."
        )


    # ----------------------------------------
    # 2. Rapid Renaming Activity
    # ----------------------------------------

    print("\n2. TIME INTERVAL ANALYSIS")
    print("----------------------------------------")

    rapid_events = 0


    for i in range(
        len(records) - 1
    ):

        current_event = records[i]

        next_event = records[i + 1]


        time_difference = (
            next_event["timestamp"]
            - current_event["timestamp"]
        ).total_seconds()


        print(
            current_event["original"],
            "->",
            next_event["original"],
            "| Interval:",
            time_difference,
            "seconds"
        )


        if time_difference <= RAPID_INTERVAL:

            rapid_events += 1


    if rapid_events >= 3:

        risk_score += 25

        print(
            "\n[WARNING] Rapid file renaming "
            "activity detected."
        )

    else:

        print(
            "\nNo significant rapid renaming "
            "pattern detected."
        )


    # ----------------------------------------
    # 3. Extension Change Analysis
    # ----------------------------------------

    print("\n3. FILE EXTENSION ANALYSIS")
    print("----------------------------------------")

    extension_changes = []


    for record in records:

        old_extension = os.path.splitext(
            record["original"]
        )[1].lower()

        new_extension = os.path.splitext(
            record["renamed"]
        )[1].lower()


        if old_extension != new_extension:

            extension_changes.append(
                (
                    record["original"],
                    record["renamed"],
                    old_extension,
                    new_extension
                )
            )


    new_extensions = Counter()

    for change in extension_changes:

        new_extensions[
            change[3]
        ] += 1


    suspicious_extension_found = False


    for extension, count in new_extensions.items():

        print(
            "New Extension:",
            extension,
            "| Files:",
            count
        )


        if count >= 3:

            suspicious_extension_found = True


    if suspicious_extension_found:

        risk_score += 30

        print(
            "[WARNING] Multiple files changed "
            "to the same extension."
        )


    # ----------------------------------------
    # 4. Directory Analysis
    # ----------------------------------------

    print("\n4. DIRECTORY ANALYSIS")
    print("----------------------------------------")

    directory_count = Counter()


    for record in records:

        directory_count[
            record["directory"]
        ] += 1


    for directory, count in directory_count.items():

        print(
            directory,
            "-",
            count,
            "files affected"
        )


    if len(directory_count) > 1:

        risk_score += 15

        print(
            "[WARNING] Multiple directories "
            "were affected."
        )


    # ----------------------------------------
    # 5. Risk Classification
    # ----------------------------------------

    print("\nRISK ASSESSMENT")
    print("========================================")

    print(
        "Risk Score:",
        risk_score,
        "/ 100"
    )


    if risk_score >= 70:

        risk_level = "HIGH RISK"

    elif risk_score >= 40:

        risk_level = "MEDIUM RISK"

    else:

        risk_level = "LOW RISK"


    print(
        "Risk Level:",
        risk_level
    )


    # ----------------------------------------
    # 6. Event Evidence
    # ----------------------------------------

    print("\nSUPPORTING EVIDENCE")
    print("----------------------------------------")


    for record in records:

        print(
            record["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "|",
            record["original"],
            "->",
            record["renamed"],
            "| Directory:",
            record["directory"]
        )


except FileNotFoundError:

    print(
        "File renaming log does not exist."
    )

except ValueError:

    print(
        "Invalid timestamp format in the log."
    )

except Exception as e:

    print("Error:", e)
