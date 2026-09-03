import hashlib
from datetime import datetime

def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


print("DIGITAL FORENSIC CASE REPORT")
print("--------------------------------")

case_number = input("Enter case number: ")
investigator = input("Enter investigator name: ")
evidence_id = input("Enter evidence ID: ")
description = input("Enter evidence description: ")
evidence_file = input("Enter evidence file: ")

try:
    hash_value = calculate_sha256(evidence_file)

    print("\nEnter Investigation Findings")
    findings = input("Findings: ")

    conclusion = input("Enter conclusion: ")
    recommendations = input("Enter recommendations: ")

    report_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
DIGITAL FORENSIC CASE REPORT
================================

Case Number       : {case_number}
Investigator      : {investigator}
Report Date       : {report_date}

EVIDENCE DETAILS
--------------------------------
Evidence ID       : {evidence_id}
Evidence File     : {evidence_file}
Description       : {description}

HASH VERIFICATION
--------------------------------
Algorithm         : SHA-256
Hash Value        : {hash_value}

INVESTIGATION FINDINGS
--------------------------------
{findings}

CONCLUSION
--------------------------------
{conclusion}

RECOMMENDATIONS
--------------------------------
{recommendations}

================================
End of Digital Forensic Report
"""

    with open("forensic_case_report.txt", "w") as file:
        file.write(report)

    print("\nCase report generated successfully.")
    print("Report saved as: forensic_case_report.txt")

    print("\n" + report)

except FileNotFoundError:
    print("Evidence file does not exist.")
