import re


password = input("Enter password: ")

# Lookahead assertions
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")



text = """Hello World
python is powerful
PYTHON is easy
"""

print("\n--- Regex Modifiers Examples ---")

# re.IGNORECASE
match_ignore = re.search(r'python', text, re.IGNORECASE)
print("IGNORECASE:", match_ignore.group())

# re.MULTILINE
match_multi = re.findall(r'^python', text, re.MULTILINE)
print("MULTILINE:", match_multi)

# re.DOTALL
match_dotall = re.search(r'Hello.*easy', text, re.DOTALL)
print("DOTALL:", match_dotall.group())
