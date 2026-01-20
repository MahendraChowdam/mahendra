import re

text = "goood cat 123"

# Meta-characters
print("Dot (.) :", re.search(r'c.t', text))
print("Star (*) :", re.search(r'go*d', text))
print("Plus (+) :", re.search(r'go+d', text))
print("Question (?) :", re.search(r'colou?r', 'color'))

# Special sequences
print("Digits (\\d):", re.findall(r'\d+', text))
print("Word (\\w):", re.findall(r'\w+', text))
print("Space (\\s):", re.findall(r'\s', text))
