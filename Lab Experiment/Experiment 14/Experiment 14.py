import hashlib

filename = "evidence.txt"

with open(filename, "rb") as file:
    data = file.read()

md5 = hashlib.md5(data).hexdigest()
sha1 = hashlib.sha1(data).hexdigest()
sha256 = hashlib.sha256(data).hexdigest()

print("MD5    :", md5)
print("SHA-1  :", sha1)
print("SHA-256:", sha256)
