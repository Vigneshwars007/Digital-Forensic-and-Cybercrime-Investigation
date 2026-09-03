import csv
import os

filename = input("Enter process execution log: ")

suspicious_names = [
    "mimikatz.exe",
    "keylogger.exe",
    "malware.exe",
    "ransomware.exe",
    "backdoor.exe"
]

suspicious_locations = [
    "\\temp\\",
    "\\appdata\\local\\temp\\",
    "/tmp/"
]

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\nSuspicious Processes")
        print("-----------------------------")

        found = False

        for row in reader:

            process = row["Process"].lower()
            path = row["Path"].lower()

            suspicious = False
            reason = ""

            # Check process name
            if process in suspicious_names:
                suspicious = True
                reason = "Suspicious process name"

            # Check execution path
            for location in suspicious_locations:
                if location in path:
                    suspicious = True
                    reason = "Suspicious execution path"

            if suspicious:
                print("\n[SUSPICIOUS PROCESS]")
                print("Process :", row["Process"])
                print("PID     :", row["PID"])
                print("User    :", row["User"])
                print("Path    :", row["Path"])
                print("Reason  :", reason)

                found = True

        if not found:
            print("No suspicious processes found.")

except FileNotFoundError:
    print("Process execution log does not exist.")
