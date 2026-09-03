import csv
from datetime import datetime
from collections import defaultdict


filename = input("Enter USB activity log file: ")

records = []


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
                "device_id": row["DeviceID"],
                "device_name": row["DeviceName"],
                "user": row["User"],
                "status": row["Status"]
            })


    # Sort records chronologically
    records.sort(
        key=lambda x: x["timestamp"]
    )


    print("\nUSB DEVICE USAGE ANALYSIS")
    print("========================================")


    # ----------------------------------------
    # Chronological Device Usage History
    # ----------------------------------------

    print("\nCHRONOLOGICAL DEVICE-USAGE HISTORY")
    print("----------------------------------------")

    for record in records:

        print(
            record["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "| Device:",
            record["device_name"],
            "| ID:",
            record["device_id"],
            "| User:",
            record["user"],
            "| Status:",
            record["status"]
        )


    # ----------------------------------------
    # Group Records by Device
    # ----------------------------------------

    devices = defaultdict(list)

    for record in records:

        devices[
            record["device_id"]
        ].append(record)


    print("\nDEVICE SUMMARY")
    print("========================================")


    for device_id, device_records in devices.items():

        first_record = device_records[0]

        users = set()

        connection_count = 0


        for record in device_records:

            users.add(record["user"])

            if record["status"].lower() == "connected":

                connection_count += 1


        previously_recognized = "Yes"

        if connection_count == 1:

            previously_recognized = "No"


        print("\nDevice Name:", first_record["device_name"])
        print("Device ID  :", device_id)

        print(
            "First Connected:",
            first_record["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        print(
            "Connection Count:",
            connection_count
        )

        print(
            "Associated Users:",
            ", ".join(sorted(users))
        )

        print(
            "Previously Recognized:",
            previously_recognized
        )


except FileNotFoundError:

    print(
        "USB activity log file does not exist."
    )

except ValueError:

    print(
        "Invalid timestamp format in the log."
    )

except Exception as e:

    print("Error:", e)
