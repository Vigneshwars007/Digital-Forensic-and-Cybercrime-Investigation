import csv
from collections import defaultdict


filename = input(
    "Enter authentication log file: "
)


# Store failed login attempts
source_attempts = defaultdict(list)


try:

    # ----------------------------------------
    # Read Authentication Log
    # ----------------------------------------

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)


        for row in reader:

            status = row["Status"].lower()


            # Analyze only failed attempts

            if status == "failed":

                source_ip = row["SourceIP"]


                source_attempts[
                    source_ip
                ].append(row)


    print(
        "\nAUTHENTICATION ATTACK ANALYSIS"
    )

    print(
        "========================================"
    )


    # ----------------------------------------
    # Analyze Each Source Address
    # ----------------------------------------

    for source_ip, attempts in (
        source_attempts.items()
    ):


        print(
            "\nSOURCE IP:",
            source_ip
        )

        print(
            "----------------------------------------"
        )


        # Store attempts for each user

        user_attempts = defaultdict(int)


        for attempt in attempts:

            username = attempt[
                "Username"
            ]

            user_attempts[
                username
            ] += 1


        unique_users = len(
            user_attempts
        )


        total_attempts = len(
            attempts
        )


        print(
            "Total Failed Attempts:",
            total_attempts
        )


        print(
            "Unique Accounts Targeted:",
            unique_users
        )


        print(
            "\nAccount Attempt Details:"
        )


        for username, count in (
            user_attempts.items()
        ):

            print(
                username,
                "-",
                count,
                "failed attempt(s)"
            )


        # ------------------------------------
        # Password Spraying Detection
        # ------------------------------------

        average_attempts = (
            total_attempts
            / unique_users
        )


        if (
            unique_users >= 3
            and average_attempts <= 2
        ):

            print(
                "\nCLASSIFICATION: "
                "PASSWORD SPRAYING"
            )


            print(
                "Finding: One source address "
                "attempted authentication against "
                "many accounts with a small number "
                "of attempts per account."
            )


        # ------------------------------------
        # Brute Force Detection
        # ------------------------------------

        elif max(
            user_attempts.values()
        ) >= 5:

            most_targeted_user = max(
                user_attempts,
                key=user_attempts.get
            )


            print(
                "\nCLASSIFICATION: "
                "BRUTE-FORCE ATTACK"
            )


            print(
                "Finding: Repeated authentication "
                "attempts were directed toward "
                "one account."
            )


            print(
                "Most Targeted Account:",
                most_targeted_user
            )


            print(
                "Failed Attempts:",
                user_attempts[
                    most_targeted_user
                ]
            )


        # ------------------------------------
        # Other Suspicious Activity
        # ------------------------------------

        else:

            print(
                "\nCLASSIFICATION: "
                "UNDETERMINED SUSPICIOUS ACTIVITY"
            )


            print(
                "Finding: Authentication failures "
                "were detected, but the pattern "
                "does not clearly match the "
                "predefined password-spraying or "
                "brute-force criteria."
            )


    # ----------------------------------------
    # Investigation Summary
    # ----------------------------------------

    print(
        "\nINVESTIGATION SUMMARY"
    )

    print(
        "========================================"
    )


    print(
        "Source Addresses Analyzed:",
        len(source_attempts)
    )


except FileNotFoundError:

    print(
        "Authentication log file does not exist."
    )


except Exception as e:

    print(
        "Error:",
        e
    )
