import csv


def load_snapshot(filename):

    data = {}

    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            data[row["Filename"]] = row["SHA256"]

    return data


baseline_file = input(
    "Enter baseline CSV file: "
)

current_file = input(
    "Enter current snapshot CSV file: "
)


try:

    baseline = load_snapshot(baseline_file)
    current = load_snapshot(current_file)

    missing_files = []
    new_files = []
    modified_files = []
    renamed_files = []


    # Find missing files
    for filename in baseline:

        if filename not in current:

            missing_files.append(filename)


    # Find new files
    for filename in current:

        if filename not in baseline:

            new_files.append(filename)


    # Find modified files
    for filename in baseline:

        if filename in current:

            if baseline[filename] != current[filename]:

                modified_files.append(filename)


    # Find possible renamed files
    for old_name in baseline:

        for new_name in current:

            if old_name != new_name:

                if (
                    baseline[old_name]
                    == current[new_name]
                ):

                    renamed_files.append(
                        (old_name, new_name)
                    )


    print("\nINTEGRITY COMPARISON REPORT")
    print("================================")

    print("\nMISSING FILES")
    print("--------------------------------")

    if missing_files:

        for filename in missing_files:

            print("[MISSING]", filename)

    else:

        print("No missing files detected.")


    print("\nNEWLY INTRODUCED FILES")
    print("--------------------------------")

    if new_files:

        for filename in new_files:

            print("[NEW]", filename)

    else:

        print("No new files detected.")


    print("\nMODIFIED FILES")
    print("--------------------------------")

    if modified_files:

        for filename in modified_files:

            print("[MODIFIED]", filename)

            print(
                "Baseline Hash:",
                baseline[filename]
            )

            print(
                "Current Hash :",
                current[filename]
            )

    else:

        print("No modified files detected.")


    print("\nPOSSIBLE RENAMED FILES")
    print("--------------------------------")

    if renamed_files:

        for old_name, new_name in renamed_files:

            print(
                "[RENAMED]",
                old_name,
                "->",
                new_name
            )

    else:

        print("No possible renamed files detected.")


except FileNotFoundError:

    print("One or more CSV files do not exist.")

except Exception as e:

    print("Error:", e)
