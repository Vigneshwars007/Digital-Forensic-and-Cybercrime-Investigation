import hashlib


evidence_inventory = []


def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def add_evidence():

    print("\nAdd Evidence")
    print("--------------------------------")

    evidence_number = input("Evidence Number: ")
    description = input("Description: ")
    source = input("Source: ")
    acquisition = input("Acquisition Method: ")
    storage = input("Storage Location: ")
    filename = input("Evidence File: ")
    status = input("Current Status: ")

    try:
        file_size = __import__("os").path.getsize(filename)
        hash_value = calculate_sha256(filename)

        record = {
            "number": evidence_number,
            "description": description,
            "source": source,
            "acquisition": acquisition,
            "storage": storage,
            "size": file_size,
            "hash": hash_value,
            "status": status
        }

        evidence_inventory.append(record)

        print("\nEvidence added successfully.")

    except FileNotFoundError:
        print("Evidence file does not exist.")


def display_evidence(records):

    if not records:
        print("\nNo evidence records found.")
        return

    print("\nEvidence Inventory")
    print("================================")

    for record in records:

        print("\nEvidence Number :", record["number"])
        print("Description     :", record["description"])
        print("Source          :", record["source"])
        print("Acquisition     :", record["acquisition"])
        print("Storage         :", record["storage"])
        print("File Size       :", record["size"], "bytes")
        print("SHA-256         :", record["hash"])
        print("Status          :", record["status"])


def search_evidence():

    keyword = input(
        "\nEnter evidence type or source to search: "
    ).lower()

    results = []

    for record in evidence_inventory:

        if (
            keyword in record["description"].lower()
            or keyword in record["source"].lower()
        ):
            results.append(record)

    display_evidence(results)


def filter_evidence():

    status = input(
        "\nEnter integrity/status to filter: "
    ).lower()

    results = []

    for record in evidence_inventory:

        if record["status"].lower() == status:
            results.append(record)

    display_evidence(results)


while True:

    print("\nDIGITAL FORENSIC EVIDENCE INVENTORY")
    print("--------------------------------")
    print("1. Add Evidence")
    print("2. Display All Evidence")
    print("3. Search Evidence")
    print("4. Filter Evidence")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_evidence()

    elif choice == "2":
        display_evidence(evidence_inventory)

    elif choice == "3":
        search_evidence()

    elif choice == "4":
        filter_evidence()

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
