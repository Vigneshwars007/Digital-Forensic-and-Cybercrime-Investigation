report = {
    "Identification": "Laptop seized from suspect.",
    "Preservation": "Evidence sealed and write-protected.",
    "Collection": "Disk image acquired using FTK Imager.",
    "Analysis": "Deleted files and browser history examined.",
    "Presentation": "Investigation findings documented."
}

print("=" * 55)
print(" DIGITAL FORENSIC INVESTIGATION REPORT")
print("=" * 55)

for stage, details in report.items():
    print(f"\n{stage}")
    print("-" * len(stage))
    print(details)

print("\nConclusion:")
print("Evidence was collected, analyzed and documented successfully.")
