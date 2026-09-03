import re

filename = input("Enter evidence text file: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # URL pattern
    urls = re.findall(
        r'https?://[^\s]+',
        text
    )

    # Email pattern
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    # IPv4 pattern
    ip_addresses = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        text
    )

    # Domain pattern
    domains = re.findall(
        r'\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b',
        text
    )

    print("\nExtracted Digital Evidence")
    print("--------------------------------")

    print("\nURLs:")
    for url in set(urls):
        print("-", url)

    print("\nEmail Addresses:")
    for email in set(emails):
        print("-", email)

    print("\nIP Addresses:")
    for ip in set(ip_addresses):
        print("-", ip)

    print("\nDomain Names:")
    for domain in set(domains):
        print("-", domain)

except FileNotFoundError:
    print("Evidence text file does not exist.")
