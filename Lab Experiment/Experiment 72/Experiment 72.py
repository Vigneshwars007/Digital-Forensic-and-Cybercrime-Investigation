import csv
from collections import Counter


def read_network_data(filename):

    records = []

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            records.append({
                "timestamp": row["Timestamp"],
                "destination": row["DestinationIP"],
                "protocol": row["Protocol"],
                "duration": float(
                    row["Duration"]
                ),
                "volume": float(
                    row["TransferVolume"]
                )
            })

    return records


baseline_file = input(
    "Enter baseline network file: "
)

current_file = input(
    "Enter current network file: "
)


try:

    # ----------------------------------------
    # Read Baseline Data
    # ----------------------------------------

    baseline_records = read_network_data(
        baseline_file
    )


    print(
        "\nOUTBOUND TRAFFIC BASELINE ANALYSIS"
    )

    print(
        "========================================"
    )


    # Destination frequency

    destination_frequency = Counter()


    # Protocol frequency

    protocol_frequency = Counter()


    total_duration = 0

    total_volume = 0


    for record in baseline_records:

        destination_frequency[
            record["destination"]
        ] += 1


        protocol_frequency[
            record["protocol"]
        ] += 1


        total_duration += record[
            "duration"
        ]


        total_volume += record[
            "volume"
        ]


    average_duration = (
        total_duration
        / len(baseline_records)
    )


    average_volume = (
        total_volume
        / len(baseline_records)
    )


    normal_protocols = set(
        protocol_frequency.keys()
    )


    print(
        "\nBASELINE CHARACTERISTICS"
    )

    print(
        "----------------------------------------"
    )


    print(
        "\nNormal Destinations:"
    )


    for destination, count in (
        destination_frequency.items()
    ):

        print(
            destination,
            "-",
            count,
            "connections"
        )


    print(
        "\nNormal Protocols:"
    )


    for protocol in normal_protocols:

        print(
            "-",
            protocol
        )


    print(
        "\nAverage Connection Duration:",
        round(average_duration, 2),
        "seconds"
    )


    print(
        "Average Transfer Volume:",
        round(average_volume, 2),
        "MB"
    )


    # ----------------------------------------
    # Read Current Dataset
    # ----------------------------------------

    current_records = read_network_data(
        current_file
    )


    print(
        "\nCURRENT TRAFFIC ANALYSIS"
    )

    print(
        "========================================"
    )


    anomalies_found = False


    for record in current_records:

        anomalies = []


        # ------------------------------------
        # Check Destination
        # ------------------------------------

        if (
            record["destination"]
            not in destination_frequency
        ):

            anomalies.append(
                "New destination not observed "
                "in baseline"
            )


        # ------------------------------------
        # Check Protocol
        # ------------------------------------

        if (
            record["protocol"]
            not in normal_protocols
        ):

            anomalies.append(
                "Unusual protocol"
            )


        # ------------------------------------
        # Check Connection Duration
        # ------------------------------------

        if (
            record["duration"]
            > average_duration * 2
        ):

            anomalies.append(
                "Connection duration exceeds "
                "normal baseline"
            )


        # ------------------------------------
        # Check Transfer Volume
        # ------------------------------------

        if (
            record["volume"]
            > average_volume * 2
        ):

            anomalies.append(
                "Transfer volume exceeds "
                "normal baseline"
            )


        # ------------------------------------
        # Display Anomaly
        # ------------------------------------

        if anomalies:

            anomalies_found = True


            print(
                "\n[ANOMALOUS OUTBOUND ACTIVITY]"
            )


            print(
                "Timestamp:",
                record["timestamp"]
            )

            print(
                "Destination:",
                record["destination"]
            )

            print(
                "Protocol:",
                record["protocol"]
            )

            print(
                "Connection Duration:",
                record["duration"],
                "seconds"
            )

            print(
                "Transfer Volume:",
                record["volume"],
                "MB"
            )


            print(
                "\nBaseline Characteristics Violated:"
            )


            for anomaly in anomalies:

                print(
                    "-",
                    anomaly
                )


    if not anomalies_found:

        print(
            "\nNo significant deviations "
            "from the baseline were detected."
        )


except FileNotFoundError:

    print(
        "One or more network data files "
        "do not exist."
    )


except ValueError:

    print(
        "Invalid numeric data found "
        "in the dataset."
    )


except Exception as e:

    print(
        "Error:",
        e
    )
