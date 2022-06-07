import collections

groceries = {"bananas": 5, "oranges": 3}

print(groceries["bananas"])  # 5

print(groceries.get("bananas"))  # 5

contacts = {
    "Joe": {"phone": "123-4567", "email": "joe@gmail.com"},
    "Jane": {"phone": "987-6543", "email": "jane@gmail.com"}
}

print(contacts.get("Joe"))

sentence = "I like German food"

word_count = {
    "I": 1,
    "like": 1,
    "German": 1,
    "food": 1
}

# add to dictionary
word_count["Kevin"] = 2
print(word_count)

# dict.items()
print(list(word_count.items()))
print(word_count.items())

# dict.keys()
print(list(word_count.keys()))
print(word_count.keys())

# dict.values()
print(list(word_count.values()))
print(word_count.values())

word_count.pop("like")
print(word_count)

word_count.popitem()  # removes the last item
print(word_count)

# dict.clear()
word_count.clear()
print(word_count)



