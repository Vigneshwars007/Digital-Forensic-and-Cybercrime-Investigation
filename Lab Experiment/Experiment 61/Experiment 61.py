import csv
from datetime import datetime
from collections import defaultdict


filename = input("Enter application activity log file: ")

records = []

try:

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            access_time = datetime.strptime(
                row["AccessTime"],
                "%Y-%m-%d %H:%M:%S"
            )

            records.append({
                "document": row["DocumentName"],
                "user": row["User"],
                "application": row["Application"],
                "access_time": access_time,
                "activity": row["ActivityType"]
            })


    # Sort records from most recent to oldest
    records.sort(
        key=lambda x: x["access_time"],
        reverse=True
    )


    print("\nRECENTLY USED DOCUMENT ANALYSIS")
    print("========================================")


    print("\nMOST RECENTLY ACCESSED DOCUMENTS")
    print("----------------------------------------")

    for record in records:

        print(
            record["access_time"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "|",
            record["document"],
            "| User:",
            record["user"],
            "| Application:",
            record["application"],
            "| Activity:",
            record["activity"]
        )


    # Group users for each document
    document_users = defaultdict(set)

    for record in records:

        document_users[
            record["document"]
        ].add(
            record["user"]
        )


    print("\nDOCUMENTS ACCESSED BY MULTIPLE USERS")
    print("----------------------------------------")

    multiple_users_found = False

    for document, users in document_users.items():

        if len(users) > 1:

            multiple_users_found = True

            print("\nDocument:", document)

            print(
                "Users:",
                ", ".join(sorted(users))
            )

            print(
                "Number of Users:",
                len(users)
            )


    if not multiple_users_found:

        print(
            "No documents accessed by multiple "
            "users were found."
        )


    print("\nACTIVITY SUMMARY")
    print("----------------------------------------")

    print(
        "Total Activity Records:",
        len(records)
    )

    print(
        "Unique Documents:",
        len(document_users)
    )


except FileNotFoundError:

    print(
        "Application activity log file does not exist."
    )

except ValueError:

    print(
        "Invalid timestamp format in log file."
    )

except Exception as e:

    print("Error:", e)
