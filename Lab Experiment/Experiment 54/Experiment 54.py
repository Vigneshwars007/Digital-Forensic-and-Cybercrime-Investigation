import hashlib
import json
import os

DATABASE_FILE = "hash_database.json"


def calculate_sha256(filename):

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def load_database():

    if os.path.exists(DATABASE_FILE):

        with open(DATABASE_FILE, "r") as file:
            return json.load(file)

    return []


def save_database(database):

    with open(DATABASE_FILE, "w") as file:

        json.dump(
            database,
            file,
            indent=4
        )


def add_file(database):

    filename = input("Enter file name: ")

    if not os.path.isfile(filename):

        print("File does not exist.")
        return

    evidence_id = input("Enter Evidence ID: ")
    description = input("Enter Description: ")

    hash_value = calculate_sha256(filename)

    record = {
        "EvidenceID": evidence_id,
        "Description": description,
        "FileName": filename,
        "SHA256": hash_value
    }

    database.append(record)

    save_database(database)

    print("\nEvidence record added successfully.")

    print("SHA-256 Hash:")
    print(hash_value)


def verify_file(database):

    filename = input("Enter file to verify: ")

    if not os.path.isfile(filename):

        print("File does not exist.")
        return

    current_hash = calculate_sha256(filename)

    print("\nCalculated SHA-256:")
    print(current_hash)

    match_found = False

    for record in database:

        if record["SHA256"] == current_hash:

            print("\n[MATCH FOUND]")
            print("Evidence ID :", record["EvidenceID"])
            print("Description :", record["Description"])
            print("Stored File :", record["FileName"])
            print("SHA-256     :", record["SHA256"])

            match_found = True

    if not match_found:

        print("\n[NO MATCH FOUND]")
        print(
            "No existing evidence record contains "
            "this SHA-256 value."
        )


def display_database(database):

    print("\nFORENSIC HASH DATABASE")
    print("================================")

    if not database:

        print("No evidence records available.")

    else:

        for record in database:

            print("\nEvidence ID :", record["EvidenceID"])
            print("Description :", record["Description"])
            print("File Name   :", record["FileName"])
            print("SHA-256     :", record["SHA256"])


database = load_database()


while True:

    print("\nFORENSIC HASH DATABASE SYSTEM")
    print("--------------------------------")
    print("1. Add Evidence File")
    print("2. Verify File")
    print("3. Display Database")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_file(database)

    elif choice == "2":

        verify_file(database)

    elif choice == "3":

        display_database(database)

    elif choice == "4":

        print("Program terminated.")
        break

    else:

        print("Invalid choice.")
