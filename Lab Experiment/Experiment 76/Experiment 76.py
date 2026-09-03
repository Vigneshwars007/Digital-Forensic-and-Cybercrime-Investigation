import os
import re
from collections import defaultdict


folder = input(
    "Enter evidence folder path: "
)


# Structure:
# indicator_type -> indicator -> file -> count

indicators = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(int)
    )
)


patterns = {

    "IP Address":
    r'\b(?:\d{1,3}\.){3}\d{1,3}\b',


    "URL":
    r'https?://[^\s]+',


    "Email":
    r'\b[A-Za-z0-9._%+-]+@'
    r'[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',


    "Crypto Address":
    r'\b(?:bc1[a-zA-Z0-9]{20,}|'
    r'[13][a-km-zA-HJ-NP-Z1-9]{25,34})\b',


    "Domain":
    r'\b(?:[A-Za-z0-9-]+\.)+'
    r'[A-Za-z]{2,}\b'
}


try:

    print(
        "\nDIGITAL EVIDENCE INDICATOR ANALYSIS"
    )

    print(
        "========================================"
    )


    files_processed = 0


    for filename in os.listdir(folder):

        if filename.endswith(".txt"):

            file_path = os.path.join(
                folder,
                filename
            )


            files_processed += 1


            with open(
                file_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                content = file.read()


            for indicator_type, pattern in (
                patterns.items()
            ):


                matches = re.findall(
                    pattern,
                    content
                )


                for indicator in matches:

                    indicators[
                        indicator_type
                    ][
                        indicator
                    ][
                        filename
                    ] += 1


    # ----------------------------------------
    # Display Results
    # ----------------------------------------

    print(
        "\nCONSOLIDATED INDICATOR REPORT"
    )

    print(
        "========================================"
    )


    for indicator_type, indicator_data in (
        indicators.items()
    ):

        print(
            "\n",
            indicator_type.upper()
        )

        print(
            "----------------------------------------"
        )


        for indicator, files in (
            indicator_data.items()
        ):

            print(
                "\nIndicator:",
                indicator
            )


            for filename, count in (
                files.items()
            ):

                print(
                    "File:",
                    filename
                )

                print(
                    "Occurrences:",
                    count
                )


    # ----------------------------------------
    # Summary
    # ----------------------------------------

    print(
        "\nINVESTIGATION SUMMARY"
    )

    print(
        "========================================"
    )


    print(
        "Files Processed:",
        files_processed
    )


    for indicator_type in indicators:

        print(
            indicator_type,
            ":",
            len(
                indicators[indicator_type]
            ),
            "unique values"
        )


except FileNotFoundError:

    print(
        "Evidence folder not found."
    )


except Exception as e:

    print(
        "Error:",
        e
    )
