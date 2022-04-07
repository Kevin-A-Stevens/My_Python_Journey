"""
************ Dictionaries and Sets ************
A Dictionary is a collection of values stored using a key
A Dictionary is storing Key:Value pairs
"""
from contents import pantry

## import this prints out the Zen of Python
import this

vehicles = {'dream': 'Honda 250T',
           'roadster': 'BMW R1100',
           'er5': 'Kawasaki ER5',
           'can-am': 'Bombardier Can-Am 250',
           'virago': 'Yamaha XV250',
           'tenere': 'Yamaha XT650',
           'jimny': 'Suzuki Jimny 1,5',
           'fiesta': 'Ford Fiesta Ghia 1.4',
           }
"""
************ Get a value using indexing ************ 
If a key does not exist using indexing, will give a KeyError
indexing is faster than the get method
"""
my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

"""
************ Get a value using the get method ************ 
If a key does not exist using the get method, returns None
"""
learner = vehicles.get("er5")
print(learner)

print("-" * 80)
"""
************ iterating over a dictionary ************ 
iterating over a dictionary will give the keys
if you want values, will need to index the dictionary
"""
for key in vehicles:
    print(key)

print("-" * 80)

for key in vehicles:
    print(key, vehicles[key])

## Make it prettier
print("-" * 80)

for key in vehicles:
    print(key, vehicles[key], sep=", ")

"""
************ iterating over a dictionary ************ 
iterating over a dictionary efficiently
.item method
remember to use enumerate when iterating over sequences
use .items() when iterating over dictionaries
"""
print("-" * 80)
for key, value in vehicles.items():
    print(key, value, sep=", ")

"""
************ adding items to a dictionary ************
dictionaries do not have an append method
"""
print("-" * 80)

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

for key, value in vehicles.items():
    print(key, value, sep=", ")

"""
************ changing values in a dictionary ************
"""
print("-" * 80)

vehicles["virago"] = "Yamaha XV535"

for key, value in vehicles.items():
    print(key, value, sep=", ")

"""
************ removing items from a dictionary ************
"""
print("-" * 80)
del vehicles["starfighter"]

for key, value in vehicles.items():
    print(key, value, sep=", ")

"""
************ removing items from a dictionary ************
Using the pop method
returns whatever you pass as the default if key does not exist
no default will crash with an error
Can also use a string to return a message
"""

print("-" * 80)
vehicles.pop("f1", None)

plane = vehicles.pop("learjet")
print(plane)
bike = vehicles.pop("tenere", "not preset")
print(bike)

"""
************ using in with a dictionary ************
using in, you are only checking thr keys
"""

available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = {}  # Create an empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")

"""
************ dictionary or list ************
dictionary code is shorter
list is more appropriate if you have to sort the values
"""

"""
************ setdefault method ************
returns the value of the key of the key exists in a dictionary
returns the default value specified if it doesn't exist
The difference between setdefault and get is that setdefault adds the item
Note that beans was added and ketchup was not added to the dictionary
"""

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

print()
print("'pantry' now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)

"""
************ more dictionary methods ************
fromkeys = useful for creating new dictionary items
keys = places keys in the form of a list
update = update a dictionary. combine a dictionary with a new dictionary
values
copy = create a copy of the original dictionary
"""
d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)

keys = d.keys()
print(keys)
"""
************ dictionary or list ************
dictionary code is shorter
list is more appropriate if you have to sort the values
"""
for item in d.keys():  # keys can be used to make a line more readable
    print(item)

d2 = {
    7: "luck seven",
    10: "ten",
    3: "this is the new three",
}

d.update(d2)
for key, value in d.items():
    print(key, value)

print()

d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)

print("-" * 80)

d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

v = d.values()
print(d)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(v)
if "four" in value:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with a key {key}")

print()

for key, values in d.items():
    if value == "four":
        print(f"{d[key]} was found with a key {key}")

lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "gray", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

things = animals.copy()
print(things["teddy"])
print(animals["teddy"])

print()

# things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)

"""
************ hash function/table ************
"""
print("-" * 80)
data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# print(ord("a"))
# print(ord("b"))
# print(ord("z"))


def simple_hash(s: str) -> int:
    """A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


# for key, value in data:
#     # h = simple_hash(key)
#     h = hash(key)
#     print(key, h)

keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()
value = get("lemon")
print(value)

print("-" * 80)

import hashlib

# See what is guaranteed and use those
print(sorted(hashlib.algorithms_guaranteed))
print(sorted(hashlib.algorithms_available))

print("-" * 80)

python_program = """for i in range(10):
print(i)
"""
print(python_program)

for b in python_program.encode('utf8'):
    print(b, chr(b))

original_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"SHA256: {original_hash.hexdigest()}")

python_program += "print('code change')"
print(python_program)

new_hash = hashlib.sha256(python_program.encode('utf8'))
print()
print(f"SHA256: {new_hash.hexdigest()}")

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been changed")
else:
    print("The code has been modified")
