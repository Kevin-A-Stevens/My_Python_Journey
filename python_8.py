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

#small_ints.remove(99)  # crashes with an error - sometimes you want an error

"""
discard method
"""
travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    # Python 3.5 and earlier
    # print("{}: {}".format(key, value))

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # travelling by plane, remove restricted items
    # for restricted_item in restricted_items:
    #     items.discard(restricted_item)
    items.difference_update(restricted_items)

# print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)

"""
remove method
"""
# drugs
amlodipine = ("amlodipine", "Blood pressure")
buspirone = ("buspirone", "Anxiety disorders")
carbimazole = ("carbimazole", "Antithyroid agent")
citalopram = ("citalopram", "Antidepressant")
edoxaban = ("edoxaban", "anti-coagulant")
erythromycin = ("erythromycin", "Antibiotic")
lusinopril = ("lusinopril", "High blood pressure")
metformin = ("metformin", "Type 2 diabetes")
methotrexate = ("methotrexate", "Rheumatoid arthritis")
paracetamol = ("paracetamol", "Painkiller")
propranol = ("propranol", "Beta blocker")
simvastatin = ("simvastatin", "High cholesterol")
warfarin = ("warfarin", "anti-coagulant")

# Drugs that shouldn't be taken together
adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]

# Patient prescriptions
patients = {
    "Anne": {methotrexate, paracetamol},
    "Bob": {carbimazole, erythromycin, methotrexate, paracetamol},
    "Charley": {buspirone, lusinopril, metformin},
    "Denise": {amlodipine, lusinopril, metformin, warfarin},
    "Eddie": {amlodipine, propranol, simvastatin, warfarin},
    "Frank": {buspirone, citalopram, propranol, warfarin},
    "Georgia": {carbimazole, edoxaban, warfarin},
    "Helmut": {erythromycin, paracetamol, propranol, simvastatin},
    "Izabella": {amlodipine, citalopram, simvastatin, warfarin},
    "John": {simvastatin},
    "Kenny": {amlodipine, citalopram, metformin},
}

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking warfarin."
              f" Please remove {patient} from the trial")
    print(patient, prescription)

"""
pop method
"""

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" :")
    prescription = patients[patient]
    print(prescription)

"""
union method
combine two sets
"""
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)
all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)

all_animals_3 = wild_animals | farm_animals  # | is the union operator
print(all_animals_3)

adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]

meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch = meds_to_watch.union(interaction)

print(sorted(meds_to_watch))

"""
union update method
"""

adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]

meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch.update(interaction)
    # meds_to_watch != interaction
print(sorted(meds_to_watch))

"""
set intersection
find common items in each set
"""
print("-" * 80)

from primes_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)

squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))
print(evens & squares)

trial_1 = {"Bob", "Charley", "Georgia", "John"}
trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}
check_set = trial_1.intersection(trial_2)
print(check_set)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)

"""
set difference
find differences in each set
"""
print("-" * 80)
print(odds.difference(primes))
print(odds - primes)  # - is the difference operator

"""
set symmetric difference
"""
morning = {"Java", "C", "Ruby", "Lisp", "C#"}
afternoon = {"Python", "C#", "Java", "C", "Ruby"}

possibly_courses = morning ^ afternoon  # ^ is symmetric difference operator
print(possibly_courses)  # {'Python', 'Lisp'}

morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

possibly_courses = set(morning).symmetric_difference(afternoon)
print(possibly_courses)

possibly_courses = set(afternoon).symmetric_difference(morning)
print(possibly_courses)

"""
supersets and subsets
"""
animals = {"Turtle", "Horse", "Robin", "Python", "Swallow", "Hedgehog", "Wren", "Aardvark", "Cat"}
birds = {"Robin", "Swallow", "Wren"}
print(f"birds is a subset of animals: {birds.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issuperset(birds)}")

# Using the operators
print(birds <= animals)
print(birds < animals)

print("-" * 80)
garden_birds = {"Swallow", "Wren", "Robin"}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

print("-" * 80)
more_birds = {"Wren", "Budgie", "Swallow"}
print(garden_birds >= more_birds)  # False

print("-" * 80)
required_skills = {"python", "github", "linux"}
candidates = {
    "anna": {"java", "linux", "windows", "github", "python", "full stack"},
    "bob": {"github", "linux", "python"},
    "carol": {"linux", "javascript", "html", "python", "github"},
    "daniel": {"pascal", "java", "c++", "github"},
    "ekani": {"html", "css", "github", "python", "linux"},
    "fenna": {"linux", "pascal", "java", "c", "lisp", "modula-2", "perl", "github"},
}

interviewees = set()
for candidate, skills in candidates.items():
    if skills.issuperset(required_skills):
        interviewees.add(candidate)

print(interviewees)


