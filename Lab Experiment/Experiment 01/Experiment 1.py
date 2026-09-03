import os
from datetime import datetime

file_path = "sample.txt"

if os.path.exists(file_path):
    creation = os.path.getctime(file_path)
    modified = os.path.getmtime(file_path)
    accessed = os.path.getatime(file_path)

    print("File Metadata")
    print("Creation Time :", datetime.fromtimestamp(creation))
    print("Modified Time :", datetime.fromtimestamp(modified))
    print("Access Time   :", datetime.fromtimestamp(accessed))
else:
    print("File not found:", file_path)
