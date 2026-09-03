import os

# File carving signature database
file_signatures = {
    "JPEG": {
        "header": b"\xFF\xD8\xFF",
        "footer": b"\xFF\xD9",
        "extension": ".jpg"
    },

    "PDF": {
        "header": b"%PDF",
        "footer": b"%%EOF",
        "extension": ".pdf"
    },

    "ZIP": {
        "header": b"PK\x03\x04",
        "footer": b"PK\x05\x06",
        "extension": ".zip"
    }
}


container = input("Enter binary container file: ")

if not os.path.isfile(container):
    print("Binary container does not exist.")
    exit()

with open(container, "rb") as file:
    data = file.read()

recovery_log = []
recovery_number = 1

print("\nForensic File Carving")
print("--------------------------------")

for file_type, signature in file_signatures.items():

    header = signature["header"]
    footer = signature["footer"]
    extension = signature["extension"]

    search_position = 0

    while True:

        start = data.find(header, search_position)

        if start == -1:
            break

        end = data.find(
            footer,
            start + len(header)
        )

        if end == -1:
            print(
                "[HEADER FOUND]",
                file_type,
                "but ending pattern was not found."
            )
            break

        end = end + len(footer)

        recovered_data = data[start:end]

        output_file = (
            "recovered_"
            + str(recovery_number)
            + extension
        )

        with open(output_file, "wb") as recovered:
            recovered.write(recovered_data)

        size = len(recovered_data)

        recovery_log.append({
            "number": recovery_number,
            "format": file_type,
            "start": start,
            "end": end,
            "size": size,
            "file": output_file
        })

        print("\n[RECOVERED]")
        print("Format :", file_type)
        print("Start  :", start)
        print("End    :", end)
        print("Size   :", size, "bytes")
        print("File   :", output_file)

        recovery_number += 1

        search_position = end


# Generate recovery log
with open("recovery_log.txt", "w") as log:

    log.write("FORENSIC FILE RECOVERY LOG\n")
    log.write("============================\n\n")

    for record in recovery_log:

        log.write(
            "Evidence No : " + str(record["number"]) + "\n"
        )

        log.write(
            "Format      : " + record["format"] + "\n"
        )

        log.write(
            "Start Offset: " + str(record["start"]) + "\n"
        )

        log.write(
            "End Offset  : " + str(record["end"]) + "\n"
        )

        log.write(
            "Estimated Size: " + str(record["size"]) + " bytes\n"
        )

        log.write(
            "Recovered File: " + record["file"] + "\n"
        )

        log.write("--------------------------------\n")

print("\nRecovery log saved as: recovery_log.txt")
