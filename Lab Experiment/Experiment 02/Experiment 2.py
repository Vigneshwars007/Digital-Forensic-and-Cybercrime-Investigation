import hashlib

filename = "evidence.txt"
hash_file = "original_hash.txt"

try:
    with open(filename, "rb") as file:
        data = file.read()

    hash_value = hashlib.sha256(data).hexdigest()

    with open(hash_file, "r", encoding="utf-8") as file:
        original_hash = file.read().strip()

    print("SHA-256 Hash:")
    print(hash_value)

    if hash_value == original_hash:
        print("\nEvidence Integrity Verified")
    else:
        print("\nEvidence Tampered")
except FileNotFoundError as e:
    print("Required file not found:", e.filename)
