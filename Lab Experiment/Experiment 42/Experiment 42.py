import os

# Basic file signature database
signatures = {
    b"%PDF": (".pdf", "PDF Document"),
    b"\xFF\xD8\xFF": (".jpg", "JPEG Image"),
    b"\x89PNG": (".png", "PNG Image"),
    b"PK\x03\x04": (".zip", "ZIP Archive"),
    b"MZ": (".exe", "Windows Executable")
}


def identify_file_type(filename):
    with open(filename, "rb") as file:
        header = file.read(8)

    for signature, details in signatures.items():

        if header.startswith(signature):
            return details, header

    return None, header


filename = input("Enter evidence file: ")

if not os.path.isfile(filename):
    print("File does not exist.")
    exit()

try:
    result, header = identify_file_type(filename)

    extension = os.path.splitext(filename)[1].lower()

    print("\nFile Signature Analysis")
    print("--------------------------------")
    print("File Name        :", os.path.basename(filename))
    print("Filename Extension:", extension)
    print("Initial Bytes    :", header.hex())

    if result is None:

        print("Detected Format  : Unknown")
        print("Warning          : No known file signature identified.")

    else:

        expected_extension, file_type = result

        print("Detected Format  :", file_type)
        print("Expected Extension:", expected_extension)

        if extension == expected_extension:

            print("Classification   : CONSISTENT")
            print("Message          : Extension matches file signature.")

        else:

            print("Classification   : INCONSISTENT")
            print(
                "Warning          : Filename extension does not "
                "match the detected file format."
            )

except Exception as e:
    print("Error:", e)
