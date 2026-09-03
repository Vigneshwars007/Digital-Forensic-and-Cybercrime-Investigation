import os

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Folder does not exist.")
    exit()

suspicious_extensions = [
    ".exe", ".bat", ".cmd", ".scr", ".vbs", ".js", ".ps1"
]

document_extensions = [
    ".pdf", ".doc", ".docx", ".xls", ".xlsx",
    ".jpg", ".jpeg", ".png", ".txt"
]

print("\nSuspicious Files")
print("-----------------------------")

found = False

for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if os.path.isfile(path):

        parts = filename.lower().split(".")

        # Check double-extension files
        if len(parts) >= 3:

            first_extension = "." + parts[-2]
            final_extension = "." + parts[-1]

            if (first_extension in document_extensions and
                    final_extension in suspicious_extensions):

                print("[DOUBLE EXTENSION] :", filename)
                found = True

        # Check suspicious final extension
        final_extension = os.path.splitext(filename)[1].lower()

        if final_extension in suspicious_extensions:
            print("[SUSPICIOUS EXTENSION] :", filename)
            found = True

if not found:
    print("No suspicious files found.")
