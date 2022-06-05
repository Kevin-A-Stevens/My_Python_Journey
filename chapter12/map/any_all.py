entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))  # True
print("any: {}".format(any(entries)))  # True

print("Iterable with a 'False' value")
entries_with_a_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_a_zero)))  # False
print("any: {}".format(any(entries_with_a_zero)))  # True
