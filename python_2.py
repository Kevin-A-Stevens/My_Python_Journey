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

"""
********** Guessing game **********
"""
answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done! You guessed it.")
    else:
        print("Sorry, you have not guessed correctly.")
else:
    print("You got it first time!")

"""
********** Conditional Operators **********
<  Less than
<=  Less than or equal to
>  Greater than
>=  Greater than or equal to
==  Equal to
!-  Not equal to
"""

age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
#     print("Have a good day at work.")

"""
********** Simplified Chain Comparison **********
"""

if 16 <= age <= 65:
    print("Have a good day at work.")
else:
    print("Enjoy your free time")

print("-" * 80)

# if age < 16 or age > 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work.")

"""
********** Boolean expressions **********
True or False
"""

day = "Monday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
else:
    print("Learn Python")

if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")

"""
********** in and not in **********
"""

parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("I don't need that letter")

activity = input("What would you like to do today? ")

## The casefold() function
## Use casefold() rather than toLowerCase when you want to compare strings
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

#  https://docs.python.org/3/library/index.html
#  https://docs.python.org/3/library/stdtypes.html
