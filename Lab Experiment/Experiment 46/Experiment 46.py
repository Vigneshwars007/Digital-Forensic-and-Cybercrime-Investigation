import os
import hashlib


def calculate_hashes(filename):

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            md5.update(data)
            sha1.update(data)
            sha256.update(data)

    return (
        md5.hexdigest(),
        sha1.hexdigest(),
        sha256.hexdigest()
    )


original = input("Enter original forensic image: ")
working_copy = input("Enter working copy: ")

if not os.path.isfile(original):
    print("Original forensic image does not exist.")
    exit()

if not os.path.isfile(working_copy):
    print("Working copy does not exist.")
    exit()


original_size = os.path.getsize(original)
working_size = os.path.getsize(working_copy)

original_md5, original_sha1, original_sha256 = \
    calculate_hashes(original)

working_md5, working_sha1, working_sha256 = \
    calculate_hashes(working_copy)


print("\nFORENSIC IMAGE INTEGRITY VERIFICATION")
print("------------------------------------------")

print("\nFile Size")
print("Original    :", original_size, "bytes")
print("Working Copy:", working_size, "bytes")

print("\nMD5")
print("Original    :", original_md5)
print("Working Copy:", working_md5)

print("\nSHA-1")
print("Original    :", original_sha1)
print("Working Copy:", working_sha1)

print("\nSHA-256")
print("Original    :", original_sha256)
print("Working Copy:", working_sha256)


print("\nVerification Results")
print("------------------------------------------")

if original_size != working_size:
    print("[MISMATCH] File size is different.")

if original_md5 != working_md5:
    print("[MISMATCH] MD5 hash is different.")

if original_sha1 != working_sha1:
    print("[MISMATCH] SHA-1 hash is different.")

if original_sha256 != working_sha256:
    print("[MISMATCH] SHA-256 hash is different.")


if (
    original_size == working_size
    and original_md5 == working_md5
    and original_sha1 == working_sha1
    and original_sha256 == working_sha256
):
    print("\nRESULT: Working copy corresponds to original.")
    print("Integrity Status: VERIFIED")

else:
    print("\nRESULT: Working copy does not correspond to original.")
    print("Integrity Status: MISMATCH DETECTED")
