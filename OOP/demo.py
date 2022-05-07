a_string = "This is \na string split\t\tand tabbed"
print(a_string)

raw_string = r"This is \na string split\t\tand tabbed"
print(raw_string)

b_string = "This is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "This is a backslash \followed by some text"
print(backslash_string)

backslash_string2 = "This is a backslash \\followed by some text"
print(backslash_string2)

error_string = r"This strings ends with a \\"

