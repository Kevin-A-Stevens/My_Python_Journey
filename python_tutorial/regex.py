import re

text = "A random string. My_Name123@website.com and more random text Yourname@web.com"

# pattern = re.compile("[Ars]")  # A, r, or s (first match only)
# pattern = re.compile("[a-z]")  # a to z (first match only)
# pattern = re.compile("[a-z]+")  # a to z (first word match only)
pattern = re.compile("[a-zA-Z0-9.-_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")  # match email

# result = pattern.search(text)
result = pattern.findall(text)

print(result)
