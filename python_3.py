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
