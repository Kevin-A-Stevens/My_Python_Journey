"""
************ Dictionaries and Sets ************
A Dictionary is a collection of values stored using a key
A Dictionary is storing Key:Value pairs
"""

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
