import csv

filename = input("Enter USB activity log: ")

# Authorized USB device IDs
authorized_devices = [
    "USB001",
    "USB002",
    "USB003"
]

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\nUSB Device Activity")
        print("-----------------------------")

        found = False

        for row in reader:

            device_id = row["DeviceID"]

            if device_id not in authorized_devices:

                print("\n[UNAUTHORIZED USB DEVICE]")
                print("Date     :", row["Date"])
                print("Time     :", row["Time"])
                print("Device   :", row["Device"])
                print("Device ID:", device_id)
                print("User     :", row["User"])

                found = True

        if not found:
            print("No unauthorized USB devices detected.")

except FileNotFoundError:
    print("USB activity log does not exist.")
