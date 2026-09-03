import os
from datetime import datetime

filename = input("Enter file name: ")

if not os.path.isfile(filename):
    print("File does not exist.")
else:
    size = os.path.getsize(filename)
    creation_time = os.path.getctime(filename)
    modification_time = os.path.getmtime(filename)
    access_time = os.path.getatime(filename)

    print("\nFile Metadata")
    print("-----------------------------")
    print("File Name       :", os.path.basename(filename))
    print("File Size       :", size, "bytes")
    print("Creation Time   :", datetime.fromtimestamp(creation_time))
    print("Modification Time:", datetime.fromtimestamp(modification_time))
    print("Access Time     :", datetime.fromtimestamp(access_time))
