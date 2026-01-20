import re

text = input("Enter the Email:")

pattern = r'[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]+'

match = re.search(pattern, text)

if match:
    print("Email found:", match.group())
else:
    print("No email found")
