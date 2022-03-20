"""
*********** Sequence Types ***********
Three types in this section are list, tuple, range
A sequence is an 'ordered' collection of items
"""

"""
*********** list ***********
Enclosed in []
[] are also used to get an index in a sequence and for slicing
Slicing a list produces another list
"""

computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print(computer_parts[0:3])
print(computer_parts[-1])

"""
*********** immutable objects ***********
types of immutable objects: int, float, bool, str, tuple, frozen set, bytes
"""

## id returns the identity of an object. This is a good way to tell if an
## object is changed or if Python has to create a new object

result = True
another_result = result
print(id(result))  # 9476448
print(id(another_result))  # 9476448

result = False
print(id(result))  # 9474016
## Python created a new ID since it cannot change the original bool value

result = "Correct"
another_result = result
print(id(result))  # 140141080736880
print(id(another_result))  # 140141080736880

result += "ish"
print(id(result))   # 139660218996656
print(id(another_result))  # 140077306520432

"""
*********** mutable objects ***********
types of mutable objects: list, dict, set, Bytearray
"""

print("-" * 80)
shopping_list = ["milk",
                 "eggs",
                 "pasta",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))  # 140620009806272
print(id(another_list))  # 140620009806272

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))  # 140631703345600

## The ID remains unchanged. Python was able to change the original list

"""
*********** Binding multiple names to a list ***********
"""

print("-" * 80)
print(another_list)

## Chain assignments - One list with a number of aliases used to refer to it
a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)

## cream is in all of the list names a through f as well
## Having 2 or 3 aliases is quite common

"""
*********** Common sequence operators ***********
"""
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

"""
min and max functions
"""
print(min(even))  # 2
print(max(even))  # 8
print(min(odd))  # 1
print(max(odd))  # 9

"""
len function
"""
print()
print(len(even))  # 4
print(len(odd))  # 5

"""
count function
"""
print()
print("mississippi".count("s"))  # 4
print("mississippi".count("iss"))  # 2

"""
*********** Appending items to a list ***********
Iterating over a list using for and enumerate
enumerate returns pairs of values, The index position and an item
list comprehension
.remove method
.append method
str() function = converts item to a string
"""

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "hdmi cable",
                   "dvd drive"
                   ]

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []  # Create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()
print(computer_parts)

"""
*********** enumerate ***********
"""
for index, character in enumerate("abcdefgh"):
    print(index, character)

"""
*********** Sorting a list ***********
.extend method = takes items from iterable you pass it and adds them to the list
.sort method
This way of sorting does NOT create a copy of the list. It just rearranges the items
"""

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)

"""
*********** Sorting other types of data ***********
Used to sort any iterable object
Returns a list
Note that the list returned is a different list so this DOES create a copy
"""

## A pangram is a sentence that contains every letter of the alphabet at least once

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print(numbers)  ## not sorted
numbers.sort()
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(numbers)  ## sorted

another_sorted_numbers = numbers.sort()  ## returns None
print(numbers)
print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)

"""
*********** Case insensitive sorting ***********
casefold
"""

case_letter = sorted("The quick brown fox jumped over the lazy dog",
                     key=str.casefold)
print(case_letter)

names = ["Graham", "John", "Terry", "Eric", "terry", "michael"]

names.sort(key=str.casefold)
print(names)

"""
*********** Creating lists ***********
.copy method
"""

print("-" * 80)
empty_list = [] # Create an empty list
even = [2, 4, 6, 8] # Create a list of values
odd = [1, 3, 5, 7, 9]
numbers = even + odd # Create a list by adding lists together
print(numbers)
sorted_numbers = sorted(numbers) # create a list from a function
print(sorted_numbers)
print(numbers)
digits = sorted("432985617") ## Create a list from another object
print(digits)
digits2 = list("678372984738") ## Create a list using the list function
print(digits2)
more_numbers = list(numbers)
print(more_numbers)
print(numbers is more_numbers) ## False meaning they are not the same list
print(numbers == more_numbers) ## True because the lists contain the same items
more_numbers2 = numbers[:] ## Create a list using a slice
print(more_numbers2)
copy_numbers = numbers.copy() ## using the copy method
print(copy_numbers)

"""
*********** Replacing an item in a list using slicing ***********
.copy method
"""

computer_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "hdmi cable",
                   "dvd drive"
                   ]
print(computer_parts)

#computer_parts[3] = "trackball"
print(computer_parts[3:])
computer_parts[3:] = ["trackball"]
print(computer_parts)
