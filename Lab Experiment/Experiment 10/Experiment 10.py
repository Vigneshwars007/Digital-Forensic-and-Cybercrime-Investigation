from email import message_from_file

with open("header.txt", "r", encoding="utf-8") as f:
    msg = message_from_file(f)

from_addr = msg.get("From")
reply_to = msg.get("Reply-To")
return_path = msg.get("Return-Path")

print("From :", from_addr)
print("Reply-To :", reply_to)
print("Return-Path:", return_path)

if reply_to and from_addr != reply_to:
    print("\nWarning: Possible spoofed sender detected.")
elif return_path and from_addr not in return_path:
    print("\nWarning: Return-Path mismatch detected.")
else:
    print("\nNo obvious spoofing indicators found.")
