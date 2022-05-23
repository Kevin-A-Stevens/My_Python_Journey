import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except ValueError:
            print("Invalid number entered. Please try again")
        finally:
            print("The finally clause always executes")


first_number = getint("Please enter the first number: ")
second_number = getint("Please enter the second number: ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("division performed successfully")

