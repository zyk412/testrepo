import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@([a-z0-9_]+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
