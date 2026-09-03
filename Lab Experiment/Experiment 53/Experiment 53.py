filename = input("Enter investigator notes file: ")

sections = {
    "OBSERVATIONS": [],
    "EVIDENCE REFERENCES": [],
    "EXAMINATION STEPS": [],
    "FINDINGS": []
}

current_section = None

try:

    with open(filename, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line in sections:
                current_section = line

            elif current_section:
                sections[current_section].append(line)


    print("\nFORENSIC EXAMINATION SUMMARY")
    print("========================================")

    print("\n1. OBSERVATIONS")
    print("----------------------------------------")

    for item in sections["OBSERVATIONS"]:
        print("-", item)


    print("\n2. EVIDENCE REFERENCES")
    print("----------------------------------------")

    for item in sections["EVIDENCE REFERENCES"]:
        print("-", item)


    print("\n3. EXAMINATION STEPS")
    print("----------------------------------------")

    for number, item in enumerate(
        sections["EXAMINATION STEPS"],
        start=1
    ):
        print(str(number) + ".", item)


    print("\n4. FINDINGS")
    print("----------------------------------------")

    for item in sections["FINDINGS"]:
        print("-", item)


    print("\nSUMMARY")
    print("----------------------------------------")

    print(
        "The investigation notes were successfully "
        "organized into a formal forensic examination summary."
    )

except FileNotFoundError:

    print("Investigator notes file does not exist.")

except Exception as e:

    print("Error:", e)
