import hashlib

def calculate_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()

filename = input("Enter evidence file: ")

baseline_hash = calculate_hash(filename)

print("\nBaseline SHA-256:")
print(baseline_hash)

input("\nPress Enter to check file integrity...")

current_hash = calculate_hash(filename)

print("\nCurrent SHA-256:")
print(current_hash)

if baseline_hash == current_hash:
    print("\nFile is unchanged.")
else:
    print("\nWARNING: Unauthorized modification detected!")
