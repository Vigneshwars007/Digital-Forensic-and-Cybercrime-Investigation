import csv


def load_permissions(filename):

    permissions = {}

    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            permissions[row["Filename"]] = row["Permission"]

    return permissions


def permission_value(permission):

    value = 0

    if permission[0] == "r":
        value += 4

    if permission[1] == "w":
        value += 2

    if permission[2] == "x":
        value += 1

    return value


baseline_file = input(
    "Enter baseline permission CSV file: "
)

current_file = input(
    "Enter current permission CSV file: "
)


try:

    baseline = load_permissions(
        baseline_file
    )

    current = load_permissions(
        current_file
    )


    print("\nFILE PERMISSION COMPARISON")
    print("========================================")


    changes_found = False


    for filename in baseline:

        if filename in current:

            old_permission = baseline[
                filename
            ]

            new_permission = current[
                filename
            ]


            if old_permission != new_permission:

                changes_found = True


                print(
                    "\nFILE:",
                    filename
                )

                print(
                    "Previous Permission:",
                    old_permission
                )

                print(
                    "Current Permission :",
                    new_permission
                )


                # Compare each permission section
                old_values = [
                    permission_value(
                        old_permission[0:3]
                    ),

                    permission_value(
                        old_permission[3:6]
                    ),

                    permission_value(
                        old_permission[6:9]
                    )
                ]


                new_values = [
                    permission_value(
                        new_permission[0:3]
                    ),

                    permission_value(
                        new_permission[3:6]
                    ),

                    permission_value(
                        new_permission[6:9]
                    )
                ]


                old_total = sum(
                    old_values
                )

                new_total = sum(
                    new_values
                )


                if new_total > old_total:

                    print(
                        "Change Type: MORE PERMISSIVE"
                    )

                    print(
                        "Forensic Relevance:"
                    )

                    print(
                        "Additional permissions may "
                        "allow unauthorized users or "
                        "processes to access or modify "
                        "the file."
                    )


                elif new_total < old_total:

                    print(
                        "Change Type: MORE RESTRICTIVE"
                    )

                    print(
                        "Forensic Relevance:"
                    )

                    print(
                        "Permissions were restricted. "
                        "This may represent a security "
                        "change or an attempt to limit "
                        "access to evidence."
                    )


                else:

                    print(
                        "Change Type: PERMISSION "
                        "MODIFIED"
                    )

                    print(
                        "Forensic Relevance:"
                    )

                    print(
                        "Permission ownership categories "
                        "changed even though the overall "
                        "permission level is similar."
                    )


    if not changes_found:

        print(
            "\nNo permission changes detected."
        )


except FileNotFoundError:

    print(
        "One or more permission files do not exist."
    )

except Exception as e:

    print("Error:", e)
