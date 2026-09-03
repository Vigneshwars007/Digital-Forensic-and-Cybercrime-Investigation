signatures = {
    b"\x89PNG\r\n\x1a\n": "PNG Image",
    b"\xff\xd8\xff": "JPEG Image",
    b"%PDF": "PDF Document",
    b"PK\x03\x04": "ZIP Archive"
}

filename = r"C:\Users\Admin\Downloads\LAB_EXPERIMENTS_EMAIL_UPDATED\LAB EXPERIMENTS\Experiment 7\sample.bin"

with open(filename, "rb") as file:
    header = file.read(8)

for sig, ftype in signatures.items():
    if header.startswith(sig):
        print("Detected File Type :", ftype)
        break
else:
    print("Unknown File Type")
