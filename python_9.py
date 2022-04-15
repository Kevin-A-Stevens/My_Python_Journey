"""
************** Input and Output **************
"""

"""
********** Reading from a text file **********
"""
jabber = open("jabberwocky.txt", "r")

for line in jabber:
    print(line.strip())  # There is also rstrip and lstrip
    # print(line, end="")
    # print(len(line))

jabber.close()  # Must close a file when finished with it after opening

print("-" * 80)
# using with, you do not need to use close. It is automatically closed
with open("jabberwocky.txt", "r") as jabber:
    for line in jabber:
        print(line.rstrip())

"""
********** Reading from a text file **********
readlines method
creates a list
"""
print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)
print(lines[-1:])

# printing poem backwards
for line in reversed(lines):
    print(line, end="")

"""
********** Reading from a text file **********
read method
creates a string
"""
print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    text = jabber.read()
print(text)

for character in reversed(text):
    print(character, end="")

"""
********** Reading from a text file **********
readline method
reads one line of a file at a time
"""
print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break

print("-" * 80)
with open("jabberwocky.txt", "r") as jabber:
    for line in jabber:
        print(line.rstrip())
        if "jubjub" in line.casefold():
            break

"""
********** Reading from a text file **********
strip
lstrip
rstrip
"""
print("-" * 80)
filename = "jabberwocky.txt"
with open(filename) as poem:
    first = poem.readline().rstrip()
print(first)

chars = "'"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

chars = "'Twasebv"
no_letters = first.strip(chars)
print(no_letters)

for character in first:
    if character in chars:
        print(f"removing '{character}'")
    else:
        break

print("-" * 80)
for character in first[::-1]:  # process backwards
    if character in chars:
        print(f"removing '{character}'")
    else:
        break

"""
********** Reading from a text file **********
removeprefix - added in python 3.9
removesuffix - added in python 3.9
"""
# print("-" * 80)
# twas_removed = first.removeprefix("'Twas")
# print(twas_removed)
#
# toves_removed = first.removesuffix("toves")
# print(toves_removed)

def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]  # return copy of string

def removesuffux(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]

twas_removed = removeprefix(first, "'Twas")
toves_removed = removesuffux(first, "toves")
print(twas_removed)
print(toves_removed)

"""
********** parsing data from a text file **********
parsing means making sense of the data
"""
input_filename = "country_info.txt"

countries = {}
with open(input_filename) as country_file:  # read (r) is the default
    country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            "name": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dialing_code": dialing,
            "timezone": timezone,
            "currency": currency,
        }
        print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        # countries[chosen_country.casefold()] = country_dict

print(countries)

while True:
    chosen_country = input("Please enter the name of a country: ").casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        print(country_data["capital"])
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == "quit":
        break


"""
********** printing data to a text file **********
"""

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

## using print
plants_filename = "flower_print.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        print(plant, file=plants)

new_list = []
with open(plants_filename) as plants:
    for plant in plants:
        new_list.append(plant.rstrip())

print(new_list)

## using write
plants_filename = "flower_write.txt"
with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant)

print(data)
string_representation = data.__str__()
print(type(string_representation))

filename = "test_numbers.txt"
with open(filename, "w")as test:
    for i in range(10):
        print(i, file=test)

"""
********** unicode **********
"""
with open("jabberwocky.txt", encoding="utf-8") as jabber:
    for line in jabber:
        print(line.rstrip())

"""
********** JSON data **********
"""
print("-" * 80)
import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

with open("test.json", "w", encoding="utf-8") as testfile:
    json.dump(languages, testfile)

with open("test.json", "r", encoding="utf-8") as testfile:
    data = json.load(testfile)
print(data)
print(data[2])

"""
https://www.ncdc.noaa.gov/cag/global/time-series
download data as json data
parsing json data from a file
"""

print("-" * 80)
json_data_source = "temperature_anomaly.json"

with open(json_data_source, encoding="utf-8") as data:
    anomalies = json.load(data)

print(anomalies["description"])

for year, value in anomalies["data"].items():
    year, value = int(year), float(value)
    print(f"{year}...{value:6.2f}")
print("*" * 80)


"""
parsing json data from the internet
https://www.ncdc.noaa.gov/cag/global/time-series/globe/land-ocean/1/7/1880-2021/data.json
"""
import urllib.request

print("-" * 80)
print("-" * 80)
json_data_source = "https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json"

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode("utf-8")
    anomalies = json.loads(data)

print(anomalies["description"])

for year, value in anomalies["data"].items():
    year, value = int(year), float(value)
    print(f"{year}...{value:6.2f}")
print("*" * 80)
