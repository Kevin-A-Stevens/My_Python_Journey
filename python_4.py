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
"""
current_choice = "-"
computer_parts = []  # Create an empty list

while current_choice != "0":
    if current_choice in "123456":
        print("adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("mouse pad")
        elif current_choice == "6":
            computer_parts.append("HDMI cable")
    else:
        print("Please add options from the list below:")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse pad")
        print("6: hdmi cable")
        print("0: to finish")
    current_choice = input()
print(computer_parts)





