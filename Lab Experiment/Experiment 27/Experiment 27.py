import os
import stat

folder = input("Enter directory path: ")

if not os.path.isdir(folder):
    print("Directory does not exist.")
    exit()

print("\nFile Permission Analysis")
print("--------------------------------")

found = False

for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if not os.path.isfile(path):
        continue

    mode = os.stat(path).st_mode

    permissions = stat.filemode(mode)

    # Check if file is writable by others
    if mode & stat.S_IWOTH:

        print("[INSECURE PERMISSION]")
        print("File        :", filename)
        print("Permissions :", permissions)
        print("Reason      : Writable by others")
        print()

        found = True

if not found:
    print("No insecure file permissions found.")
