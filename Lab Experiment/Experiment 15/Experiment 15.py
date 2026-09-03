import os
import time

folder = input("Enter folder to monitor: ")

if not os.path.isdir(folder):
    print("Folder does not exist.")
    exit()

def get_files():
    files = {}

    for name in os.listdir(folder):
        path = os.path.join(folder, name)

        if os.path.isfile(path):
            files[path] = (
                os.path.getmtime(path),
                os.path.getatime(path)
            )

    return files


previous = get_files()

print("\nMonitoring folder...")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        time.sleep(2)

        current = get_files()

        # Detect created files
        for file in current:
            if file not in previous:
                print("[CREATED] ", file)

        # Detect deleted files
        for file in previous:
            if file not in current:
                print("[DELETED] ", file)

        # Detect modified/accessed files
        for file in current:
            if file in previous:

                old_mtime, old_atime = previous[file]
                new_mtime, new_atime = current[file]

                if new_mtime != old_mtime:
                    print("[MODIFIED]", file)

                if new_atime != old_atime:
                    print("[ACCESSED]", file)

        previous = current

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
