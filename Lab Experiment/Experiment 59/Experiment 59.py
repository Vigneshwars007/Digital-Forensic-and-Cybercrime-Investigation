import os
import re


suspicious_extensions = [
    ".exe",
    ".bat",
    ".cmd",
    ".scr",
    ".com",
    ".ps1",
    ".vbs",
    ".js"
]

legitimate_extensions = [
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".jpg",
    ".jpeg",
    ".png",
    ".zip",
    ".xlsx"
]


def analyze_filename(filename):

    warnings = []

    name, extension = os.path.splitext(filename)

    # Check suspicious executable extension
    if extension.lower() in suspicious_extensions:

        warnings.append(
            "Executable or script extension detected: "
            + extension
        )

    # Check multiple extensions
    parts = filename.split(".")

    if len(parts) > 2:

        warnings.append(
            "Multiple extensions detected."
        )

    # Check executable hidden behind legitimate extension
    if len(parts) > 2:

        previous_extension = "." + parts[-2].lower()

        if (
            previous_extension in legitimate_extensions
            and extension.lower()
            in suspicious_extensions
        ):

            warnings.append(
                "Possible disguised executable: "
                + filename
            )

    # Check leading or trailing spaces
    if filename != filename.strip():

        warnings.append(
            "Leading or trailing spaces detected."
        )

    # Check spaces before extension
    if re.search(r"\s+\.", filename):

        warnings.append(
            "Misleading space before extension detected."
        )

    # Check Unicode characters
    for character in filename:

        if ord(character) > 127:

            warnings.append(
                "Non-ASCII or Unicode character detected."
            )

            break

    # Check unusual symbols
    if re.search(
        r"[@#$%^&*+=~`{}[\]|<>]",
        filename
    ):

        warnings.append(
            "Unusual symbol detected in filename."
        )

    return warnings


folder = input(
    "Enter directory path to analyze: "
)


if not os.path.isdir(folder):

    print("Directory does not exist.")

else:

    print("\nSUSPICIOUS FILENAME ANALYSIS")
    print("================================")

    suspicious_found = False


    for root, directories, files in os.walk(folder):

        for filename in files:

            warnings = analyze_filename(
                filename
            )

            if warnings:

                suspicious_found = True

                filepath = os.path.join(
                    root,
                    filename
                )

                print("\nOriginal Filename:")
                print(filename)

                print("Location:")
                print(filepath)

                print("\nWarnings:")

                for warning in warnings:

                    print("-", warning)


    if not suspicious_found:

        print(
            "\nNo suspicious filename patterns "
            "were detected."
        )
