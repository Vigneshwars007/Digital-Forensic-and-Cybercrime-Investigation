import hashlib
from datetime import datetime


def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def add_custody_transfer(history):
    print("\nAdd Custody Transfer")

    handler = input("Enter handler/investigator name: ")
    action = input("Enter action performed: ")
    location = input("Enter storage location: ")

    transfer_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    history.append({
        "handler": handler,
        "action": action,
        "location": location,
        "time": transfer_time
    })

    print("Custody transfer added successfully.")


def display_history(evidence, history, current_hash):
    print("\nDIGITAL FORENSIC CHAIN OF CUSTODY")
    print("==========================================")

    print("Evidence ID      :", evidence["id"])
    print("Description      :", evidence["description"])
    print("Source           :", evidence["source"])
    print("Acquisition Time :", evidence["acquisition"])
    print("Investigator     :", evidence["investigator"])
    print("Storage Location :", evidence["storage"])
    print("Original SHA-256 :", evidence["hash"])

    print("\nCUSTODY TRANSFER HISTORY")
    print("------------------------------------------")

    for number, record in enumerate(history, start=1):

        print("\nTransfer", number)
        print("Handler   :", record["handler"])
        print("Action    :", record["action"])
        print("Time      :", record["time"])
        print("Location  :", record["location"])

    print("\nFINAL INTEGRITY VERIFICATION")
    print("------------------------------------------")

    print("Original SHA-256 :", evidence["hash"])
    print("Current SHA-256  :", current_hash)

    if evidence["hash"] == current_hash:
        print("Integrity Status : CONSISTENT")
    else:
        print("Integrity Status : MISMATCH DETECTED")


# Main program

print("FORENSIC EVIDENCE MANAGEMENT")
print("------------------------------------------")

evidence_id = input("Enter evidence ID: ")
description = input("Enter evidence description: ")
source = input("Enter evidence source: ")
investigator = input("Enter investigator name: ")
storage = input("Enter storage location: ")
filename = input("Enter evidence file: ")

try:

    original_hash = calculate_sha256(filename)

    acquisition_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    evidence = {
        "id": evidence_id,
        "description": description,
        "source": source,
        "investigator": investigator,
        "storage": storage,
        "acquisition": acquisition_time,
        "hash": original_hash
    }

    custody_history = []

    print("\nInitial evidence record created.")
    print("Original SHA-256:", original_hash)

    while True:

        print("\n1. Add Custody Transfer")
        print("2. Final Examination")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_custody_transfer(custody_history)

        elif choice == "2":

            current_hash = calculate_sha256(filename)

            display_history(
                evidence,
                custody_history,
                current_hash
            )

            break

        elif choice == "3":

            print("Program terminated.")
            break

        else:

            print("Invalid choice.")

except FileNotFoundError:

    print("Evidence file does not exist.")
