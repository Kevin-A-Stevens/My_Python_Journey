"""
******** Nested Lists & Code Style
https://peps.python.org/pep-0008/
"""
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

print("-" * 80)

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))

print("-" * 80)

"""
******** Processing Nested Lists *********
"""

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

print()
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()

"""
******** Built-in functions *********
https://docs.python.org/3/library/functions.html
revisiting the print function using keyword arguments
"""
name = "Kevin"
age = 54
print(name, age, "Python", 2022)
print(name, age, "Python", 2022, sep=", ")

print("-" * 80)
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()

## Using a generator removes the trailing comma
print("-" * 80)
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)

"""
******** More methods *********
.join method of the str class
"""
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))

print("-" * 80)
flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

separator = ",  "
output = separator.join(flowers)
print(output)
