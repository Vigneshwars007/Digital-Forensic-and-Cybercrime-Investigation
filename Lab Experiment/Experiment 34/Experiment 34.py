import csv

filename = input("Enter domain list file: ")

suspicious_keywords = [
    "login",
    "verify",
    "secure",
    "account",
    "password",
    "free",
    "update"
]

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        print("\nDomain Reputation Analysis")
        print("--------------------------------")

        found = False

        for row in reader:

            domain = row["Domain"].lower()
            reasons = []

            # Check suspicious keywords
            for keyword in suspicious_keywords:
                if keyword in domain:
                    reasons.append(
                        "Suspicious keyword: " + keyword
                    )

            # Check unusually long domain
            if len(domain) > 35:
                reasons.append("Unusually long domain")

            # Check excessive hyphens
            if domain.count("-") >= 3:
                reasons.append("Multiple hyphens")

            if reasons:

                print("\n[SUSPICIOUS DOMAIN]")
                print("Domain :", row["Domain"])

                print("Reason :")
                for reason in reasons:
                    print(" -", reason)

                found = True

        if not found:
            print("No suspicious domains found.")

except FileNotFoundError:
    print("Domain list file does not exist.")
