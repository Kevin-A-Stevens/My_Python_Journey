"""
********** code blocks **********
Notice the first line in the code block ends in a :
"""

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
print("*" * 80)

"""
********** if statements **********
"""

## int function = changes input string to int
## Using int and input combination is common when you want a number from a user
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years".format(18 - age))

"""
********** elif statements **********
"""
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda")
else:
    print("You are old enough to vote")



