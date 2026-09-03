import os
import time
from collections import Counter


def get_snapshot(folder):

    snapshot = {}

    for root, directories, files in os.walk(folder):

        for filename in files:

            filepath = os.path.join(root, filename)

            try:

                snapshot[filepath] = {
                    "modified": os.path.getmtime(filepath),
                    "size": os.path.getsize(filepath)
                }

            except FileNotFoundError:
                pass

    return snapshot


folder = input("Enter directory to monitor: ")

if not os.path.isdir(folder):

    print("Directory does not exist.")
    exit()


print("\nCreating initial file-system snapshot...")

previous_snapshot = get_snapshot(folder)

event_number = 1

created_count = 0
modified_count = 0
deleted_count = 0

affected_files = Counter()

print("\nFILE-SYSTEM ACTIVITY MONITOR")
print("--------------------------------")
print("Monitoring directory:", folder)
print("Press Ctrl + C to stop monitoring.\n")


try:

    while True:

        time.sleep(2)

        current_snapshot = get_snapshot(folder)

        # Detect created files
        for filepath in current_snapshot:

            if filepath not in previous_snapshot:

                print(
                    f"Event {event_number}: CREATED - {filepath}"
                )

                affected_files[filepath] += 1

                created_count += 1
                event_number += 1

        # Detect modified files
        for filepath in current_snapshot:

            if filepath in previous_snapshot:

                old_data = previous_snapshot[filepath]
                new_data = current_snapshot[filepath]

                if (
                    old_data["modified"]
                    != new_data["modified"]
                    or old_data["size"]
                    != new_data["size"]
                ):

                    print(
                        f"Event {event_number}: MODIFIED - {filepath}"
                    )

                    affected_files[filepath] += 1

                    modified_count += 1
                    event_number += 1

        # Detect deleted files
        for filepath in previous_snapshot:

            if filepath not in current_snapshot:

                print(
                    f"Event {event_number}: DELETED - {filepath}"
                )

                affected_files[filepath] += 1

                deleted_count += 1
                event_number += 1

        previous_snapshot = current_snapshot


except KeyboardInterrupt:

    print("\n\nMonitoring stopped.")


print("\nFILE-SYSTEM ACTIVITY SUMMARY")
print("================================")

print("Files Created :", created_count)
print("Files Modified:", modified_count)
print("Files Deleted :", deleted_count)

print("\nMOST FREQUENTLY AFFECTED FILES")
print("--------------------------------")

if affected_files:

    for filepath, count in affected_files.most_common():

        print(filepath, "-", count, "event(s)")

else:

    print("No file-system events detected.")
