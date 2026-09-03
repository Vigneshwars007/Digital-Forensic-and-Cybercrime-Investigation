import os

# Predefined file signature database
signatures = {
    b"%PDF": "PDF Document",
    b"\xFF\xD8\xFF": "JPEG Image",
    b"\x89PNG\r\n\x1a\n": "PNG Image",
    b"PK\x03\x04": "ZIP Archive",
    b"MZ": "Windows Executable",
    b"GIF8": "GIF Image",
    b"RIFF": "RIFF File"
}


def ascii_representation(data):
    result = ""

    for byte in data:

        if 32 <= byte <= 126:
            result += chr(byte)
        else:
            result += "."

    return result


filename = input("Enter evidence file: ")

if not os.path.isfile(filename):
    print("File does not exist.")
    exit()

try:

    with open(filename, "rb") as file:
        data = file.read(32)

    print("\nBinary File Analysis")
    print("--------------------------------")

    print("File Name :", os.path.basename(filename))
    print("Bytes Read:", len(data))

    print("\nHexadecimal Representation:")
    print(data.hex(" "))

    print("\nASCII Representation:")
    print(ascii_representation(data))

    detected_format = None

    for signature, file_format in signatures.items():

        if data.startswith(signature):
            detected_format = file_format
            break

    print("\nFile Format Analysis")
    print("--------------------------------")

    if detected_format:

        print("Detected Format :", detected_format)
        print("Signature       :", data[:len(signature)].hex(" "))
        print("Status          : Known signature identified")

    else:

        print("Detected Format : Unknown")
        print("Status          : No known signature identified")

except Exception as e:

    print("Error:", e)
