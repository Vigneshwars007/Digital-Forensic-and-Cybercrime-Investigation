import os
import hashlib
from collections import defaultdict


def calculate_sha256(filepath):

    sha256 = hashlib.sha256()

    try:

        with open(filepath, "rb") as file:

            while True:

                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except Exception as e:

        print("Cannot process:", filepath)
        return None


folder = input("Enter directory path: ")

if not os.path.isdir(folder):

    print("Directory does not exist.")
    exit()


file_groups = defaultdict(list)


print("\nScanning files...")
print("--------------------------------")


for root, directories, files in os.walk(folder):

    for filename in files:

        filepath = os.path.join(
            root,
            filename
        )

        hash_value = calculate_sha256(filepath)

        if hash_value:

            try:

                file_size = os.path.getsize(
                    filepath
                )

                file_groups[hash_value].append(
                    {
                        "name": filename,
                        "path": filepath,
                        "size": file_size
                    }
                )

            except FileNotFoundError:

                pass


print("\nIDENTICAL FILE ANALYSIS")
print("================================")


duplicate_found = False


for hash_value, files in file_groups.items():

    if len(files) > 1:

        duplicate_found = True

        print("\nIDENTICAL FILE GROUP")
        print("--------------------------------")

        print("SHA-256 Hash:")
        print(hash_value)

        print("\nFiles:")

        for file_info in files:

            print("\nFile Name :", file_info["name"])
            print("File Size :", file_info["size"], "bytes")
            print("Location  :", file_info["path"])


if not duplicate_found:

    print(
        "\nNo identical files were detected."
    )


print("\nANALYSIS COMPLETE")
