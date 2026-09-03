report = {
    "Case ID": "DF-2026-001",
    "Examiner": "Forensic Analyst",
    "Evidence": "Laptop Disk Image",
    "Findings": "Deleted files recovered and suspicious browser history identified.",
    "Conclusion": "Digital evidence supports the investigation."
}

print("=" * 50)
print("DIGITAL FORENSIC REPORT")
print("=" * 50)

for key, value in report.items():
    print(f"{key}: {value}")
