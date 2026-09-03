sender = ""
subject = ""
body = ""

with open("email.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.lower().startswith("from:"):
            sender = line.split(":", 1)[1].strip()
        elif line.lower().startswith("subject:"):
            subject = line.split(":", 1)[1].strip()
        elif line.lower().startswith("body:"):
            body = line.split(":", 1)[1].strip()

score = 0
suspicious_domains = ["@gmail.com", "@yahoo.com", "@hotmail.com"]
subject_keywords = ["urgent", "verify", "winner", "lottery", "account",
                    "bank", "congratulations", "free"]
body_keywords = ["click here", "login now", "verify account", "update password",
                 "free gift", "bank details", "limited time", "claim prize",
                 "confirm account"]

for domain in suspicious_domains:
    if sender.lower().endswith(domain):
        score += 1

for word in subject_keywords:
    if word in subject.lower():
        score += 1

for word in body_keywords:
    if word in body.lower():
        score += 1

print("Sender:", sender)
print("Subject:", subject)
print("Phishing Score:", score)
print("Result:", "PHISHING EMAIL DETECTED" if score >= 3 else "LEGITIMATE EMAIL")
