import csv

filename = input("Enter malware activity log: ")

suspicious_files = [
    ".exe",
    ".bat",
    ".scr",
    ".vbs",
    ".ps1"
]

suspicious_processes = [
    "malware.exe",
    "keylogger.exe",
    "ransomware.exe",
    "backdoor.exe"
]

suspicious_ips = [
    "203.0.113.25",
    "198.51.100.50",
    "10.10.10.50"
]

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\nMalware Activity Analysis")
        print("--------------------------------")

        found = False

        for row in reader:

            event_type = row["EventType"]
            details = row["Details"]
            reason = None

            if event_type == "File":
                if any(ext in details for ext in suspicious_files):
                    reason = "Suspicious file extension"

            elif event_type == "Process":
                if any(proc in details for proc in suspicious_processes):
                    reason = "Suspicious process"

            elif event_type == "Network":
                if any(ip in details for ip in suspicious_ips):
                    reason = "Suspicious network destination"

            if reason:
                found = True
                print("\n[SUSPICIOUS ACTIVITY]")
                print("Date       :", row["Date"])
                print("Time       :", row["Time"])
                print("Event Type :", event_type)
                print("Details    :", details)
                print("Reason     :", reason)

        if not found:
            print("No suspicious activity detected.")

except FileNotFoundError:
    print("Malware activity log does not exist.")

except Exception as e:
    print("Error:", e)
