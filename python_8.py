"""
*********** Sets ***********
An unordered collection with no duplicate entries
You cannot index into a set
"""
farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}

if more_animals == farm_animals:
    print("The sets are equal")
else:
    print("The sets are different")

"""
*********** adding items to a set ***********
add method
"""

numbers0 = {}
print(numbers0, type(numbers0))  # dict

numbers1 = {*""}
# numbers1 = {*{}} also creates an empty set
# numbers1 = set() also creates an empty set
print(numbers1, type(numbers1))  # set

numbers1.add(1)
print(numbers1)

while len(numbers1) < 4:
    next_value = int(input("Please enter your next number: "))
    numbers1.add(next_value)
print(numbers1)

"""
*********** using a set to remove duplicate values ***********
"""

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
unique_data1 = (set(data))  # creates a set
unique_data2 = sorted(set(data))  # creates a list as when ordering, sets are ruled out
print(unique_data1)
print(unique_data2)

"""
*********** create a list of unique colors, keeping the order they appear ***********
"""
unique_data3 = list(dict.fromkeys(data))
print(unique_data3)

print("-" * 80)
print(dict.fromkeys(data))

"""
*********** deleting items to a set ***********
clear method = clears all items in a set
discard method
remove method
pop method
"""

small_ints = set(range(21))
print(small_ints)

small_ints.clear()
print(small_ints)

small_ints = set(range(21))
small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)
print(small_ints)

small_ints.remove(99)  # crashes with an error - sometimes you want an error


