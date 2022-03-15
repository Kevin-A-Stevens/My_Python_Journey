"""
********** for loops **********
"""
parrot = "Norwegian Blue"

for character in parrot:
    print(character)

number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

## isnumeric() string method = returns True if the item is numeric and False otherwise
for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

## Using the sum function
values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

"""
********** iterating over a range **********
"""

## The range function
for i in range(1, 21):
    print("i is now {}".format(i))

# Coding challenge
for i in range(10):
    print(i)

# using step value with range - need a start value specified
for i in range(0, 10, 2):
    print("i is now {}".format(i))

print("-" * 80)

# counting backwards
for i in range(10, 0, -2):
    print("i is now {}".format(i))

# Coding challenge
for i in range(0, 100, 7):
    print(i)

"""
********** nested for loops **********
"""

## multiplication table
for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("-" * 20)

"""
********** continue **********
interrupt the normal flow of the loop, to either jump out of it or stop
the current iteration and move on to the next one
"""

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

## continue skips the item spam and continues to next item
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)

"""
********** break **********
breaks out of the loop completely
"""
print("-" * 80)
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)

item_to_find = "spam"
found_at = None

"""
Finding an item in a list
"""

print("-" * 80)
## The len function provides how many items are in a list
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("Item found at position {}".format(found_at))

"""
Initializing variables and None
"""
print("-" * 80)

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatross"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index  # Must be initialized outside of the for loop above
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

"""
********** while loops **********
"""
print("-" * 80)
i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("I bet you are glad to be out of there")

"""
********** Guessing game **********
"""
print("-" * 80)

"""
The random module
"""

import random

highest = 10
answer = random.randint(1, highest)
guess = 0  # Initialize to any number that does not equal the answer
print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done! You guessed it.")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

"""
********** Hi-Lo game **********
The pass keyword = doesn't do anything but makes the code syntactically correct
pass if often used as a place holder
"""
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("press ENTER to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        # pass
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess
        # pass
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c")

    guesses += 1
else:
    print("You thought of a number {}".format(low))
    print("I got it in {} guesses".format(guesses))

"""
********** else in a loop **********
Pay attention to the indentation
The else is on the same level as the for loop
"""
numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        print("The number is unacceptable")
        break
else:
    print("All of the numbers are fine")

"""
********** Augmented assignment **********
The combination in a single statement of a binary operation and an assignment 
statement. Ex guesses += 1
"""

"""
********** Style Guide PEP8 **********
https://peps.python.org/pep-0008/
"""
