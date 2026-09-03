import hashlib
import shutil

source = "evidence.txt"
destination = "evidence_copy.txt"

shutil.copy2(source, destination)

def calculate_hash(filename):
    sha = hashlib.sha256()
    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()

original_hash = calculate_hash(source)
copied_hash = calculate_hash(destination)

print("Original SHA-256 :", original_hash)
print("Copied SHA-256   :", copied_hash)

if original_hash == copied_hash:
    print("Integrity Verified")
else:
    print("Integrity Check Failed")
