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

"""
******** More methods *********
.split method = splits a string into words
"""
panagram = """The quick brown
 fox jumps\t over
  the lazy dog"""
words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

"""
******** Tuples *********
An ordered set of data
Note the parentheses
tuples are immutable
"""
t = ("a", "b", "c")
print(t)

name = "Kevin"
age = 54
print(name, age, "Python", 2022)
print((name, age, "Python", 2022))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

"""
******** Unpacking Tuples *********
"""

a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76 # data represents a tuple
print(data)
x, y, z = data
print(x)
print(y)
print(z)

## Note that you can unpack alist but may not be a good idea
## If the list adds or removes and item prior to unpacking
## The program will crash
print("Unpacking a list")
data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)

# for index, character in enumerate("abcdefg"):
#     print(index, character)

for t in enumerate("abcdefgh"):
    print(t)

print("-" * 80)
title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee Table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)

"""
******** Nested Tuples and Lists *********
"""

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))  # Our list contains 5 tuples

## for loop unpacking a tuple
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print("-" * 80)
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for name, artist, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs: {}"
          .format(name, artist, year, songs))

print()
"""
******** Nested Tuples and Lists *********
"""
album = albums[3]
print(album)

songs = album[3]
print(songs)

song = songs[2]
print(song)

print(song[1])

mayhem = albums[3][3][2][1]
print(mayhem)

print(albums[3])
print(albums[3][3])
print(albums[3][3][2])
print(albums[3][3][2][1])

print("-" * 80)
print("-" * 80)

"""
******** Simple Jukebox *********
"""
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

## Capitals represent a constant and you shouldn't change it
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
    print("=" * 40)




