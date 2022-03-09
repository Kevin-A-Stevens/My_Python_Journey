"""
Python is named after Monty Python's Flying Circus

Python supports several programming paradigms and can be used for
Procedural programming, Functional programming, and Object Oriented
programming

programming Paradigm = a style of programming

Creator is Guido van Rossum who worked at Google for 7 years
"""

# My first Python program

"""
********** printing in Python **********
print function - prints outputs to screen
"""
print('Hello, World!')

"""
'Hello, World!' is the argument passed to the print function
The comma can be used to separate arguments
Can also print out calculations
"""

print(1 + 2)
print(7 * 6)
print()
print("The end", "or is it?", "keep watching to learn more about Python", 3)

"""
Coding exercise 1
"""

print("My hovercraft is full of eels")
print(6 * 7)

"""
********** Strings in Python **********
Can be enclosed in either "" or ''
"""

print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')

# String concatenation
print("hello" + " world")

# Variables
greeting = "Hello"
name = "Kevin"

print(greeting + " " + name)
print(greeting, name)  # The comma can be used as a space

"""
input function
"""
# Asking for user input
name = input("Please enter your name ")
print(greeting, name)

"""
The Escape character \n and \t and \
"""

split_string = "This string has been\nsplit\nover\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# or
print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)

another_split_string = """This string has been
split over
several lines"""

print(another_split_string)

another_split_string2 = """This string has been \
split over \
several lines"""

print(another_split_string2)

"""
Coding exercise
"""

print("Number 1\tThe Larch\nNumber 2\tThe Horse Chestnut")

# Include the \ character in your string
# Ctrl-D to duplicate a line
#print("C:\Users\kevinstevens\notes.txt")
print("C:\\Users\\kevinstevens\\notes.txt")
print(r"C:\Users\kevinstevens\notes.txt")

"""
********** Variables in Python **********
"""

age = 54
print(age)

"""
The type function - describes the kind of information we are storing
"""
print(type(greeting))
print(type(age))

"""
********** Numeric data types **********
int - whole numbers with no fractional part
float - real numbers with a fractional part
complex
"""

"""
********** Numeric operators **********
"""

a = 12
b = 3

print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # integer division rounds down
print(a % b) # modulo or remainder

print()

"""
The range function - must be integers
"""
for i in range(1, 4):
    print(i) # 1 2 3

"""
Coding challenge
"""
bun_price = 2.40
money = 15
bun_amount = 15 // 2.40
print(bun_amount)

"""
********** Operator Precedence **********
division/multiplication has higher precedence than addition/subtraction
PEMDAS
Parentheses
Exponents
Multiplication/Division
Addition/Subtraction
"""

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))

"""
********** The str String Data Type **********
"""

parrot = "Norwegian Blue"
print(parrot)

# print an index position
print(parrot[3]) # w
print(parrot[4]) # e
print(parrot[9]) # space
print(parrot[3]) # w
print(parrot[6]) # i
print(parrot[8]) # n

"""
********** Negative indexing **********
"""

print()
print(parrot[-1])  # e
print(parrot[-14]) # N

"""
********** Slicing **********
start, stop, step
Note the last character is not included in the slice
"""

parrot = "Norwegian Blue"
print(parrot)

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])  # Norwegian - do not need to provide a start value starting at 0
print(parrot[10:])  # Blue - do not need to provide an end value to rest of string

print(parrot[:6]) # starts at beginning of string
print(parrot[6:]) # ends at end of string
print(parrot[:6] + parrot[6:])  # Norwegian Blue
print(parrot[:]) # prints entire string

"""
********** Slicing with negative numbers **********
Counts from end of string
"""
print(parrot[-4:-2])  # Bl
print(parrot[-14:-8]) # Norweg

"""
********** Slicing using step **********
number of characters to skip
"""
print(parrot)
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223;373:036 854,775;807"
seperators = number[1::4]  # ,,,,,,
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])  # [9, 223, 373, 36, 854, 775, 807]


"""
********** Slicing backwards **********
"""
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]  # step of -1 counts backwards
print(backwards)

## A sequence of ::-1 is a Python Idiom of reversing a sequence

"""
Coding challenge
"""

## Other idioms
qpo = letters[16:13:-1]
print(qpo)
edbca = letters[4::-1]
print(edbca)
last_eight_reverse = letters[:-9:-1]
print(last_eight_reverse)

## Return last n items from string
print(letters[-4:])
## Return the last item in a string
print(letters[-1:])
## Return the first item in a string
print(letters[:1])
print(letters[0]) # works if the string is not empty

"""
********** String Operators **********
"""
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

# print a string n times
print("Hello " * 5)

today = "Tuesday"
print("day" in today)
print("Tue" in today)
print("Fri" in today)

"""
********** String Replacement Fields **********
"""

## str function changes the variable into a string

age = 54
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))  # Using replacement field
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}".format(
    31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"
))

"""
********** String Formatting **********
{0:2} = use 2 digits
{1:<3} = use 3 spaces and left aligned
{2:^4} = use 4 spaces and centered
formatting makes the output easier to read
"""

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

"""
Floating point numbers
{0:12} = default prints 15 decimals
{0:12f} = floating point gives the default 6 digits
{0:12.50f} = floating point with a precision of 50 digits after decimal point
{0:52.50f} = same as above but higher field widths
{0:62.50f} = same as above but higher field widths
{0:<72.50f} = same as above but higher field widths left aligned
"""
print("Pi is approx {0:12}".format(22 / 7))
print("Pi is approx {0:12f}".format(22 / 7))
print("Pi is approx {0:12.50f}".format(22 / 7))
print("Pi is approx {0:52.50f}".format(22 / 7))
print("Pi is approx {0:62.50f}".format(22 / 7))
print("Pi is approx {0:<72.50f}".format(22 / 7))
print("Pi is approx {0:<72.54f}".format(22 / 7))

"""
********** f strings **********
New in Python 3.6
"""

age_in_words = "8 years"
print(name + f" is {age} years old")

print(f"Pi is approximately {22 / 7:12.50f}")

"""
********** String Interpolation **********
Has been deprecated and removed at some point
"""

age = 54
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("Pi is approximately %f" % (22 / 7))
print("Pi is approximately %60.50f" % (22 / 7))
