import csv
import os


# ----------------------------------------
# Function to Read CSV Files
# ----------------------------------------

def read_csv(filename):

    records = []

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                records.append(row)

    except FileNotFoundError:

        print(
            "Warning:",
            filename,
            "not found."
        )

    return records


# ----------------------------------------
# Input Files
# ----------------------------------------

evidence_file = input(
    "Enter evidence inventory CSV file: "
)

custody_file = input(
    "Enter custody records CSV file: "
)

metadata_file = input(
    "Enter metadata CSV file: "
)

hash_file = input(
    "Enter hash verification CSV file: "
)

timeline_file = input(
    "Enter investigation timeline CSV file: "
)

findings_file = input(
    "Enter analytical findings CSV file: "
)

recommendations_file = input(
    "Enter recommendations text file: "
)


# ----------------------------------------
# Read Evidence Files
# ----------------------------------------

evidence_records = read_csv(
    evidence_file
)

custody_records = read_csv(
    custody_file
)

metadata_records = read_csv(
    metadata_file
)

hash_records = read_csv(
    hash_file
)

timeline_records = read_csv(
    timeline_file
)

findings_records = read_csv(
    findings_file
)


# ----------------------------------------
# Read Recommendations
# ----------------------------------------

recommendations = []


try:

    with open(
        recommendations_file,
        "r",
        encoding="utf-8"
    ) as file:

        recommendations = [
            line.strip()
            for line in file
            if line.strip()
        ]


except FileNotFoundError:

    print(
        "Warning: Recommendations file "
        "not found."
    )


# ----------------------------------------
# Mandatory Evidence Fields
# ----------------------------------------

mandatory_fields = [

    "EvidenceID",
    "Description",
    "Source",
    "StorageLocation",
    "HashValue",
    "Status"

]


# ----------------------------------------
# Check Incomplete Evidence
# ----------------------------------------

incomplete_records = []


for record in evidence_records:

    missing_fields = []


    for field in mandatory_fields:

        if (
            field not in record
            or not record[field].strip()
        ):

            missing_fields.append(
                field
            )


    if missing_fields:

        incomplete_records.append({

            "EvidenceID":
            record.get(
                "EvidenceID",
                "UNKNOWN"
            ),

            "Missing":
            missing_fields

        })


# ----------------------------------------
# Create Output Dossier
# ----------------------------------------

output_file = "forensic_case_dossier.txt"


with open(
    output_file,
    "w",
    encoding="utf-8"
) as report:


    # ------------------------------------
    # Case Header
    # ------------------------------------

    report.write(
        "DIGITAL FORENSIC CASE DOSSIER\n"
    )

    report.write(
        "=" * 60
        + "\n\n"
    )


    # ------------------------------------
    # Evidence Inventory
    # ------------------------------------

    report.write(
        "1. EVIDENCE INVENTORY\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if evidence_records:

        for record in evidence_records:

            report.write(
                "\nEvidence ID: "
                + record.get(
                    "EvidenceID",
                    "Not Available"
                )
                + "\n"
            )


            report.write(
                "Description: "
                + record.get(
                    "Description",
                    "Not Available"
                )
                + "\n"
            )


            report.write(
                "Source: "
                + record.get(
                    "Source",
                    "Not Available"
                )
                + "\n"
            )


            report.write(
                "Storage Location: "
                + record.get(
                    "StorageLocation",
                    "Not Available"
                )
                + "\n"
            )


            report.write(
                "Hash Value: "
                + record.get(
                    "HashValue",
                    "Not Available"
                )
                + "\n"
            )


            report.write(
                "Status: "
                + record.get(
                    "Status",
                    "Not Available"
                )
                + "\n"
            )


    else:

        report.write(
            "No evidence inventory records available.\n"
        )


    # ------------------------------------
    # Custody Records
    # ------------------------------------

    report.write(
        "\n2. CHAIN OF CUSTODY RECORDS\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if custody_records:

        for record in custody_records:

            report.write(
                str(record)
                + "\n"
            )

    else:

        report.write(
            "No custody records available.\n"
        )


    # ------------------------------------
    # Metadata
    # ------------------------------------

    report.write(
        "\n3. METADATA INFORMATION\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if metadata_records:

        for record in metadata_records:

            report.write(
                str(record)
                + "\n"
            )

    else:

        report.write(
            "No metadata records available.\n"
        )


    # ------------------------------------
    # Hash Verification
    # ------------------------------------

    report.write(
        "\n4. HASH VERIFICATION RESULTS\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if hash_records:

        for record in hash_records:

            report.write(
                str(record)
                + "\n"
            )

    else:

        report.write(
            "No hash verification records available.\n"
        )


    # ------------------------------------
    # Investigation Timeline
    # ------------------------------------

    report.write(
        "\n5. INVESTIGATION TIMELINE\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if timeline_records:

        for record in timeline_records:

            report.write(
                str(record)
                + "\n"
            )

    else:

        report.write(
            "No timeline records available.\n"
        )


    # ------------------------------------
    # Analytical Findings
    # ------------------------------------

    report.write(
        "\n6. ANALYTICAL FINDINGS\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if findings_records:

        for record in findings_records:

            report.write(
                str(record)
                + "\n"
            )

    else:

        report.write(
            "No analytical findings available.\n"
        )


    # ------------------------------------
    # Recommendations
    # ------------------------------------

    report.write(
        "\n7. RECOMMENDATIONS\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if recommendations:

        for number, recommendation in enumerate(

            recommendations,
            start=1

        ):

            report.write(

                str(number)
                + ". "
                + recommendation
                + "\n"

            )

    else:

        report.write(
            "No recommendations available.\n"
        )


    # ------------------------------------
    # Missing Information
    # ------------------------------------

    report.write(
        "\n8. INCOMPLETE EVIDENCE RECORDS\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    if incomplete_records:


        report.write(
            "The following evidence records "
            "contain missing mandatory information:\n"
        )


        for record in incomplete_records:


            report.write(
                "\nEvidence ID: "
                + record["EvidenceID"]
                + "\n"
            )


            report.write(
                "Missing Fields: "
                + ", ".join(
                    record["Missing"]
                )
                + "\n"
            )


    else:

        report.write(
            "All evidence records contain "
            "the required information.\n"
        )


    # ------------------------------------
    # Final Summary
    # ------------------------------------

    report.write(
        "\n9. CASE SUMMARY\n"
    )

    report.write(
        "-" * 60
        + "\n"
    )


    report.write(
        "Total Evidence Records: "
        + str(
            len(evidence_records)
        )
        + "\n"
    )


    report.write(
        "Custody Records: "
        + str(
            len(custody_records)
        )
        + "\n"
    )


    report.write(
        "Metadata Records: "
        + str(
            len(metadata_records)
        )
        + "\n"
    )


    report.write(
        "Hash Verification Records: "
        + str(
            len(hash_records)
        )
        + "\n"
    )


    report.write(
        "Timeline Records: "
        + str(
            len(timeline_records)
        )
        + "\n"
    )


    report.write(
        "Analytical Findings: "
        + str(
            len(findings_records)
        )
        + "\n"
    )


    report.write(
        "Incomplete Evidence Records: "
        + str(
            len(incomplete_records)
        )
        + "\n"
    )


# ----------------------------------------
# Display Completion Message
# ----------------------------------------

print(
    "\nFORENSIC CASE DOSSIER CREATED"
)

print(
    "========================================"
)

print(
    "Output File:",
    output_file
)

print(
    "Evidence Records:",
    len(evidence_records)
)

print(
    "Incomplete Records:",
    len(incomplete_records)
)
