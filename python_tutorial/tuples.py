# l = []
# t = ()

t = (1,2,3)
print(t[0])

credit_card1 = (123456789, "Kevin Stevens", "11/20", 123)
credit_card2 = (123456789, "Kevin Stevens", "11/20", 123)

credit_cards = [credit_card1, credit_card2]
print(credit_cards)

# Unpacking a tuple
person1 = ("Kevin", 55, "German Food")
person2 = ("Steve", 50, "Pizza")

people = [person1, person2]

(name, age, fav_food) = person1
print(name)
print(age)
print(fav_food)

for name, age, fav_food in people:
    print(name)
    print(age)
    print(fav_food)
    print()
