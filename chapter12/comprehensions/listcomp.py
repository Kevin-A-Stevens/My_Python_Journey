print(__file__)

numbers = [1,2,3,4,5,6]

number = int(input("Please enter a number and I'll tell you its square: "))

squares = [number ** 2 for number in numbers]
# squares = [number ** 2 for number in range(1, 7)]

index_pos = numbers.index(number)
print(squares[index_pos])

# List comprehension in 2 parts
# 1. expression (number ** 2)
# 2. iteration (for number in numbers)

