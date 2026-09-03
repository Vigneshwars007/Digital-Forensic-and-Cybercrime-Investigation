import csv

filename = input("Enter simulated email mailbox: ")

suspicious_domains = [
    "unknown-mail.com",
    "fake-login.com",
    "suspicious-domain.net"
]

suspicious_keywords = [
    "urgent",
    "verify",
    "password",
    "account",
    "payment",
    "security alert"
]

suspicious_extensions = [
    ".exe",
    ".bat",
    ".scr",
    ".vbs",
    ".js",
    ".zip"
]

emails = []

try:
    with open(filename, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            score = 0
            reasons = []

            sender = row["Sender"].lower()
            subject = row["Subject"].lower()
            attachment = row["Attachment"].lower()
            url = row["URL"].lower()

            # Check sender domain
            for domain in suspicious_domains:

                if domain in sender:
                    score += 3
                    reasons.append("Suspicious sender domain")

            # Check subject
            for keyword in suspicious_keywords:

                if keyword in subject:
                    score += 1
                    reasons.append(
                        "Suspicious subject keyword: " + keyword
                    )

            # Check attachment
            for extension in suspicious_extensions:

                if attachment.endswith(extension):
                    score += 3
                    reasons.append(
                        "Suspicious attachment type"
                    )

            # Check URL
            if "http://" in url or "https://" in url:

                if any(domain in url for domain in suspicious_domains):
                    score += 3
                    reasons.append("Suspicious embedded URL")

            emails.append({
                "score": score,
                "reasons": reasons,
                "row": row
            })

    # Highest score first
    emails.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("\nEmail Forensic Analysis")
    print("--------------------------------")

    found = False

    for email in emails:

        if email["score"] >= 3:

            row = email["row"]

            print("\n[EMAIL REQUIRING ATTENTION]")
            print("Score      :", email["score"])
            print("Sender     :", row["Sender"])
            print("Recipient  :", row["Recipient"])
            print("Timestamp  :", row["Timestamp"])
            print("Subject    :", row["Subject"])
            print("Attachment :", row["Attachment"])
            print("URL        :", row["URL"])

            print("Reasons:")
            for reason in email["reasons"]:
                print(" -", reason)

            found = True

    if not found:
        print("No emails requiring forensic attention found.")

except FileNotFoundError:
    print("Email mailbox file does not exist.")
