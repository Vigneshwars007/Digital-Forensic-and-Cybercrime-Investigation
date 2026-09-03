import csv
from collections import defaultdict


filename = input(
    "Enter network log file: "
)

threshold = int(
    input(
        "Enter destination threshold: "
    )
)


source_destinations = defaultdict(set)


try:

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            source_ip = row["SourceIP"]
            destination_ip = row["DestinationIP"]


            source_destinations[
                source_ip
            ].add(
                destination_ip
            )


    print("\nNETWORK COMMUNICATION ANALYSIS")
    print("========================================")


    # ----------------------------------------
    # Count and rank source addresses
    # ----------------------------------------

    ranked_sources = sorted(
        source_destinations.items(),
        key=lambda item: len(item[1]),
        reverse=True
    )


    print(
        "\nSOURCE ADDRESS RANKING"
    )

    print("----------------------------------------")


    for source_ip, destinations in ranked_sources:

        destination_count = len(
            destinations
        )


        print(
            "\nSource IP:",
            source_ip
        )

        print(
            "Unique Destinations:",
            destination_count
        )


        # Flag sources exceeding threshold

        if destination_count > threshold:

            print(
                "Status: FLAGGED"
            )

            print(
                "Reason: Source communicated "
                "with more destinations than "
                "the investigator-defined threshold."
            )

        else:

            print(
                "Status: Normal"
            )


    # ----------------------------------------
    # Display detailed flagged sources
    # ----------------------------------------

    print(
        "\nFLAGGED SOURCE ADDRESSES"
    )

    print("========================================")


    flagged_found = False


    for source_ip, destinations in ranked_sources:

        if len(destinations) > threshold:

            flagged_found = True


            print(
                "\n[FLAGGED]"
            )

            print(
                "Source IP:",
                source_ip
            )

            print(
                "Number of Unique Destinations:",
                len(destinations)
            )

            print(
                "Destination Systems:"
            )


            for destination in sorted(
                destinations
            ):

                print(
                    "-",
                    destination
                )


    if not flagged_found:

        print(
            "No source addresses exceeded "
            "the defined threshold."
        )


except FileNotFoundError:

    print(
        "Network log file does not exist."
    )

except ValueError:

    print(
        "Please enter a valid number "
        "for the threshold."
    )

except Exception as e:

    print(
        "Error:",
        e
    )
