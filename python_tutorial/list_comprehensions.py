names = ["Billy", "Kevin", "Sally", "Jennifer"]

# for loop
l = []
for person in names:
    l.append(person)
print(l)

# list comp
print([person for person in names])

n = []
for person in names:
    n.append(person + ' dumped me')
print(n)

# list comp
print([person + ' dumped me' for person in names])

movies_and_ratings = {
    "Intersteller": 7,
    "Dark Knight": 8,
    "50 shades": 3,
    "Jurassic Park": 8,
}

s = []
for movie in movies_and_ratings:
    if movies_and_ratings[movie] > 6:
        s.append(movie)
print(s)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])
