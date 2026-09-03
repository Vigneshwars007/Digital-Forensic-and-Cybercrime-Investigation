import csv
from collections import Counter
from urllib.parse import urlparse

filename = input("Enter browser history file: ")

urls = []

try:
    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            url = row["URL"]
            urls.append(url)

    # Count website visits
    website_count = Counter()

    for url in urls:
        domain = urlparse(url).netloc
        website_count[domain] += 1

    print("\nFrequently Visited Websites")
    print("-----------------------------")

    for website, count in website_count.most_common():
        print(website, ":", count, "visits")

    # Suspicious URL indicators
    suspicious_words = [
        "login",
        "verify",
        "password",
        "free-money",
        "malware",
        "phishing",
        "account-alert"
    ]

    print("\nSuspicious URLs")
    print("-----------------------------")

    found = False

    for url in urls:

        lower_url = url.lower()

        for word in suspicious_words:

            if word in lower_url:
                print("[SUSPICIOUS] :", url)
                found = True
                break

    if not found:
        print("No suspicious URLs found.")

except FileNotFoundError:
    print("Browser history file does not exist.")
