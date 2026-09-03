import os
import hashlib

folder = input("Enter evidence folder: ")

if not os.path.isdir(folder):
    print("Folder does not exist.")
    exit()

hashes = {}

for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if os.path.isfile(path):

        with open(path, "rb") as file:
            data = file.read()

        sha256 = hashlib.sha256(data).hexdigest()

        if sha256 in hashes:
            hashes[sha256].append(filename)
        else:
            hashes[sha256] = [filename]

print("\nDuplicate Digital Evidence Files")
print("--------------------------------")

found = False

for sha256, files in hashes.items():

    if len(files) > 1:
        found = True

        print("\nDuplicate Files:")
        for file in files:
            print(" -", file)

        print("SHA-256:", sha256)

if not found:
    print("No duplicate files found.")
