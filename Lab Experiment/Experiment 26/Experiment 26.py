import os
import stat

folder = input("Enter directory path: ")

if not os.path.isdir(folder):
    print("Directory does not exist.")
    exit()

print("\nHidden and Suspicious Files")
print("--------------------------------")

found = False

for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if not os.path.isfile(path):
        continue

    hidden = False
    reason = ""

    # Check Linux/macOS hidden file convention
    if filename.startswith("."):
        hidden = True
        reason = "Hidden file name"

    # Check Windows hidden attribute
    try:
        attributes = os.stat(path).st_file_attributes

        if attributes & stat.FILE_ATTRIBUTE_HIDDEN:
            hidden = True
            reason = "Windows hidden attribute"

    except AttributeError:
        pass

    if hidden:
        print("[HIDDEN FILE]")
        print("File   :", filename)
        print("Reason :", reason)
        print()

        found = True

if not found:
    print("No hidden files found.")
