import csv
from collections import defaultdict


filename = input(
    "Enter firewall log file: "
)

threshold = int(
    input(
        "Enter repeated attempt threshold: "
    )
)


blocked_attempts = defaultdict(list)


try:

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            action = row["Action"].lower()


            # Analyze only blocked records

            if action == "blocked":

                key = (
                    row["SourceIP"],
                    row["DestinationPort"]
                )


                blocked_attempts[
                    key
                ].append(row)


    print(
        "\nFIREWALL LOG INVESTIGATION"
    )

    print(
        "========================================"
    )


    print(
        "\nBLOCKED CONNECTION SUMMARY"
    )

    print(
        "----------------------------------------"
    )


    persistent_findings = []


    for key, records in blocked_attempts.items():

        source_ip = key[0]

        destination_port = key[1]

        attempt_count = len(records)


        print(
            "\nSource IP:",
            source_ip
        )

        print(
            "Destination Port:",
            destination_port
        )

        print(
            "Blocked Attempts:",
            attempt_count
        )


        if attempt_count >= threshold:

            print(
                "Status: PERSISTENT ACTIVITY"
            )


            persistent_findings.append(
                (
                    source_ip,
                    destination_port,
                    records
                )
            )

        else:

            print(
                "Status: Low Activity"
            )


    # ----------------------------------------
    # Significant Findings
    # ----------------------------------------

    print(
        "\nMOST SIGNIFICANT FINDINGS"
    )

    print(
        "========================================"
    )


    if persistent_findings:

        # Sort findings by number of attempts

        persistent_findings.sort(
            key=lambda item: len(item[2]),
            reverse=True
        )


        for source_ip, port, records in persistent_findings:

            print(
                "\n[PERSISTENT RESTRICTED ACCESS]"
            )

            print(
                "Source IP:",
                source_ip
            )

            print(
                "Destination Port:",
                port
            )

            print(
                "Total Attempts:",
                len(records)
            )

            print(
                "\nAttempt Timestamps:"
            )


            for record in records:

                print(
                    "-",
                    record["Timestamp"],
                    "| Destination:",
                    record["DestinationIP"]
                )


    else:

        print(
            "No persistent unauthorized "
            "access attempts detected."
        )


except FileNotFoundError:

    print(
        "Firewall log file does not exist."
    )

except ValueError:

    print(
        "Please enter a valid numeric threshold."
    )

except Exception as e:

    print(
        "Error:",
        e
    )
