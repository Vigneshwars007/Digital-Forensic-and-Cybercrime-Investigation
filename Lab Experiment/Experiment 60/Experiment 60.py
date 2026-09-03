import csv
from datetime import datetime
from collections import Counter
from urllib.parse import urlparse


filename = input("Enter browser history CSV file: ")

start_date = input(
    "Enter start date (YYYY-MM-DD): "
)

end_date = input(
    "Enter end date (YYYY-MM-DD): "
)

suspicious_url = input(
    "Enter suspicious URL keyword: "
).lower()


records = []


try:

    start_time = datetime.strptime(
        start_date,
        "%Y-%m-%d"
    )

    end_time = datetime.strptime(
        end_date + " 23:59:59",
        "%Y-%m-%d %H:%M:%S"
    )


    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            if start_time <= timestamp <= end_time:

                url = row["URL"]

                domain = urlparse(url).netloc

                records.append(
                    {
                        "timestamp": timestamp,
                        "url": url,
                        "domain": domain
                    }
                )


    # Sort records chronologically
    records.sort(
        key=lambda x: x["timestamp"]
    )


    print("\nBROWSER ACTIVITY ANALYSIS")
    print("================================")


    print("\nCHRONOLOGICAL BROWSING ACTIVITY")
    print("--------------------------------")

    for record in records:

        print(
            record["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "|",
            record["url"]
        )


    # First visits
    print("\nFIRST VISITS")
    print("--------------------------------")

    visited_domains = set()

    for record in records:

        domain = record["domain"]

        if domain not in visited_domains:

            print(
                domain,
                "-",
                record["timestamp"].strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )

            visited_domains.add(domain)


    # Repeated visits
    domain_count = Counter()

    for record in records:

        domain_count[
            record["domain"]
        ] += 1


    print("\nREPEATED VISITS")
    print("--------------------------------")

    repeated_found = False

    for domain, count in domain_count.items():

        if count > 1:

            print(
                domain,
                "-",
                count,
                "visits"
            )

            repeated_found = True


    if not repeated_found:

        print(
            "No repeated visits detected."
        )


    # Most active browsing periods
    hour_count = Counter()

    for record in records:

        hour = record[
            "timestamp"
        ].strftime("%H:00")

        hour_count[hour] += 1


    print("\nMOST ACTIVE BROWSING PERIODS")
    print("--------------------------------")

    for hour, count in hour_count.most_common():

        print(
            hour,
            "-",
            count,
            "activities"
        )


    # Suspicious URL context
    print("\nSUSPICIOUS URL ANALYSIS")
    print("--------------------------------")

    suspicious_found = False


    for index, record in enumerate(records):

        if suspicious_url in record["url"].lower():

            suspicious_found = True

            print(
                "\nSuspicious URL:",
                record["url"]
            )

            print(
                "Time:",
                record["timestamp"]
            )


            if index > 0:

                previous_record = records[
                    index - 1
                ]

                print(
                    "\nAccessed Before:"
                )

                print(
                    previous_record["url"]
                )


            if index < len(records) - 1:

                next_record = records[
                    index + 1
                ]

                print(
                    "\nAccessed After:"
                )

                print(
                    next_record["url"]
                )


    if not suspicious_found:

        print(
            "No matching suspicious URL found."
        )


except FileNotFoundError:

    print(
        "Browser history file does not exist."
    )

except ValueError:

    print(
        "Invalid date or timestamp format."
    )

except Exception as e:

    print("Error:", e)
