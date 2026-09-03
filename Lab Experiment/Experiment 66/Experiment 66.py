import os


folder = input(
    "Enter directory path to analyze: "
)


# Predefined suspicious directory names
suspicious_directory_names = [
    "temp_hidden",
    "secret",
    "unknown",
    "backup_hidden",
    "system_files"
]


# Unusual file size threshold
LARGE_FILE_SIZE = 100 * 1024 * 1024


ordinary_hidden = []
requires_examination = []


try:

    if not os.path.isdir(folder):

        print("Directory does not exist.")
        exit()


    print("\nCONCEALED INFORMATION ANALYSIS")
    print("========================================")


    for root, directories, files in os.walk(folder):


        # Analyze directories
        for directory in directories:

            directory_path = os.path.join(
                root,
                directory
            )


            if directory.startswith("."):

                ordinary_hidden.append(
                    (
                        directory_path,
                        "Hidden directory indicator detected"
                    )
                )


            if (
                directory.lower()
                in suspicious_directory_names
            ):

                requires_examination.append(
                    (
                        directory_path,
                        "Unusual or suspicious directory name"
                    )
                )


        # Analyze files
        for filename in files:

            filepath = os.path.join(
                root,
                filename
            )


            try:

                file_size = os.path.getsize(
                    filepath
                )


                # Hidden filename indicator
                if filename.startswith("."):

                    ordinary_hidden.append(
                        (
                            filepath,
                            "Filename begins with hidden "
                            "file indicator (.)"
                        )
                    )


                # Zero-size file
                if file_size == 0:

                    requires_examination.append(
                        (
                            filepath,
                            "Zero-size file detected"
                        )
                    )


                # Unusually large file
                if file_size > LARGE_FILE_SIZE:

                    requires_examination.append(
                        (
                            filepath,
                            "Unusually large file: "
                            + str(file_size)
                            + " bytes"
                        )
                    )


                # Unusual filename pattern
                if (
                    filename.count(".") > 2
                ):

                    requires_examination.append(
                        (
                            filepath,
                            "Multiple extensions detected"
                        )
                    )


            except PermissionError:

                print(
                    "Permission denied:",
                    filepath
                )

            except FileNotFoundError:

                pass


    # ----------------------------------------
    # Ordinary Hidden Objects
    # ----------------------------------------

    print("\nORDINARY HIDDEN OBJECTS")
    print("----------------------------------------")


    if ordinary_hidden:

        for item, reason in ordinary_hidden:

            print("\nObject:", item)
            print("Reason:", reason)

    else:

        print(
            "No ordinary hidden objects detected."
        )


    # ----------------------------------------
    # Items Requiring Further Examination
    # ----------------------------------------

    print(
        "\nITEMS REQUIRING FURTHER EXAMINATION"
    )

    print("----------------------------------------")


    if requires_examination:

        for item, reason in requires_examination:

            print("\nObject:", item)
            print("Reason:", reason)

    else:

        print(
            "No suspicious concealed objects detected."
        )


    # ----------------------------------------
    # Summary
    # ----------------------------------------

    print("\nANALYSIS SUMMARY")
    print("========================================")

    print(
        "Ordinary Hidden Objects:",
        len(ordinary_hidden)
    )

    print(
        "Items Requiring Examination:",
        len(requires_examination)
    )


except Exception as e:

    print("Error:", e)
