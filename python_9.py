"""
************** Input and Output **************
"""

"""
********** Reading from a text file **********
"""
jabber = open("jabberwocky.txt", "r")

for line in jabber:
    print(line.strip())  # There is also rstrip and lstrip
    # print(line, end="")
    # print(len(line))

jabber.close()  # Must close a file when finished with it after opening

print("-" * 80)
# using with, you do not need to use close. It is automatically closed
with open("jabberwocky.txt", "r") as jabber:
    for line in jabber:
        print(line.rstrip())

"""
********** Reading from a text file **********
readlines method
creates a list
"""
print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)
print(lines[-1:])

# printing poem backwards
for line in reversed(lines):
    print(line, end="")

"""
********** Reading from a text file **********
read method
creates a string
"""
print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    text = jabber.read()
print(text)

for character in reversed(text):
    print(character, end="")

"""
********** Reading from a text file **********
readline method
reads one line of a file at a time
"""
print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break

print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    for line in jabber:
        print(line.rstrip())
        if "jubjub" in line.casefold():
            break

"""
********** Reading from a text file **********
strip
lstrip
rstrip
"""
print("-" * 80)
filename = "jabberwocky.txt"
with open(filename) as poem:
    first = poem.readline().rstrip()
print(first)

chars = "'"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

chars = "'Twasebv"
no_letters = first.strip(chars)
print(no_letters)

for character in first:
    if character in chars:
        print(f"removing '{character}'")
    else:
        break

print("-" * 80)
for character in first[::-1]:  # process backwards
    if character in chars:
        print(f"removing '{character}'")
    else:
        break

"""
********** Reading from a text file **********
removeprefix - added in python 3.9
removesuffix - added in python 3.9
"""
# print("-" * 80)
# twas_removed = first.removeprefix("'Twas")
# print(twas_removed)
#
# toves_removed = first.removesuffix("toves")
# print(toves_removed)

def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]  # return copy of string

def removesuffux(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]

twas_removed = removeprefix(first, "'Twas")
toves_removed = removesuffux(first, "toves")
print(twas_removed)
print(toves_removed)

"""
********** parsing data from a text file **********
parsing means making sense of the data
"""
input_filename = "country_info.txt"

with open(input_filename) as country_file:  # read (r) is the default
    for row in country_file:
        data = row.strip("\n").split("|")
        print(data)


