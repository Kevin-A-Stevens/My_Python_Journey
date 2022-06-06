# l = []
# t = ()
# s = {}

list_of_numbers = [1, 2, 3, 3, 4, 4, 4, 5]

no_duplicate_set = set(list_of_numbers)
print(no_duplicate_set)
no_duplicate_list = list(no_duplicate_set)
print(no_duplicate_list)
list_of_numbers = no_duplicate_list
print(list_of_numbers)

s = {'blueberry', 'rasberry'}

s.add("strawberry")

print(s)

library1 = {"Harry Potter", "Hunger Games", "Lord of the Rings"}
library2 = {"Harry Potter", "Romeo and Juliet"}

all_books_in_town = library1.union(library2)
print(all_books_in_town)

common_books_in_town = library1.intersection(library2)
print(common_books_in_town)

different_books_in_town1 = library1.difference(library2)
print(different_books_in_town1)

different_books_in_town2 = library2.difference(library1)
print(different_books_in_town2)
