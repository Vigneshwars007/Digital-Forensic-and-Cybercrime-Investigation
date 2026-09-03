import csv
from datetime import datetime, timedelta
from collections import defaultdict


filename = input(
    "Enter packet log file: "
)

window_seconds = int(
    input(
        "Enter time window in seconds: "
    )
)


records = []


try:

    # ----------------------------------------
    # Read Packet Records
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

            records.append({
                "timestamp": timestamp,
                "source": row["SourceIP"],
                "destination": row["DestinationIP"]
            })


    if not records:

        print("No packet records found.")
        exit()


    # ----------------------------------------
    # Sort Records
    # ----------------------------------------

    records.sort(
        key=lambda x: x["timestamp"]
    )


    print(
        "\nPACKET TRAFFIC ANALYSIS"
    )

    print(
        "========================================"
    )


    # ----------------------------------------
    # Create Time Windows
    # ----------------------------------------

    start_time = records[0]["timestamp"]

    windows = defaultdict(list)


    for record in records:

        difference = (
            record["timestamp"]
            - start_time
        ).total_seconds()


        window_number = int(
            difference // window_seconds
        )


        windows[
            window_number
        ].append(record)


    # ----------------------------------------
    # Calculate Average Packet Count
    # ----------------------------------------

    total_packets = len(records)

    total_windows = len(windows)


    average_packets = (
        total_packets
        / total_windows
    )


    print(
        "\nTRAFFIC WINDOW STATISTICS"
    )

    print(
        "----------------------------------------"
    )


    print(
        "Average Packets Per Window:",
        round(average_packets, 2)
    )


    # ----------------------------------------
    # Analyze Each Window
    # ----------------------------------------

    spike_threshold = (
        average_packets * 2
    )


    suspicious_windows = []


    for window_number in sorted(
        windows.keys()
    ):

        packet_list = windows[
            window_number
        ]

        packet_count = len(
            packet_list
        )


        window_start = (
            start_time
            + timedelta(
                seconds=
                window_number
                * window_seconds
            )
        )


        window_end = (
            window_start
            + timedelta(
                seconds=window_seconds
            )
        )


        print(
            "\nTime Window:"
        )

        print(
            window_start.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "to",
            window_end.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )


        print(
            "Packet Count:",
            packet_count
        )


        if packet_count >= spike_threshold:

            print(
                "Status: TRAFFIC SPIKE DETECTED"
            )


            suspicious_windows.append(
                (
                    window_start,
                    window_end,
                    packet_list
                )
            )

        else:

            print(
                "Status: Normal"
            )


    # ----------------------------------------
    # Analyze Destination IPs
    # ----------------------------------------

    print(
        "\nPOSSIBLE DoS PATTERN ANALYSIS"
    )

    print(
        "========================================"
    )


    if suspicious_windows:


        for (
            window_start,
            window_end,
            packet_list
        ) in suspicious_windows:


            destination_count = Counter()


            for packet in packet_list:

                destination_count[
                    packet["destination"]
                ] += 1


            print(
                "\n[SUSPICIOUS TRAFFIC WINDOW]"
            )


            print(
                "Time Period:",
                window_start.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "to",
                window_end.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )


            print(
                "Total Packets:",
                len(packet_list)
            )


            print(
                "\nDestination Statistics:"
            )


            for (
                destination,
                count
            ) in (
                destination_count.items()
            ):


                print(
                    destination,
                    "-",
                    count,
                    "packets"
                )


            # Find destination with
            # highest packet count

            top_destination = max(
                destination_count,
                key=destination_count.get
            )


            top_count = (
                destination_count[
                    top_destination
                ]
            )


            print(
                "\nMost Targeted Destination:",
                top_destination
            )

            print(
                "Packets Directed:",
                top_count
            )


            if (
                top_count
                >= len(packet_list) * 0.7
            ):

                print(
                    "Finding: A large percentage "
                    "of packets were directed toward "
                    "the same destination."
                )

                print(
                    "Possible DoS attack pattern "
                    "requires further investigation."
                )


    else:

        print(
            "No significant traffic spikes "
            "were detected."
        )


except FileNotFoundError:

    print(
        "Packet log file does not exist."
    )


except ValueError:

    print(
        "Invalid timestamp or time "
        "window value."
    )


except Exception as e:

    print(
        "Error:",
        e
    )
