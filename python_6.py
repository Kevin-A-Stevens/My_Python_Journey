"""
************ Functions ************
A function that is bound to an instance of a class is called a Method
"""

"""
************ Defining a function ************
"""


def multiply(x: float, y: float) -> float:
    """
   Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()
for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

"""
************ Palindromes ************
A palindrome is a word that reads the same both backwards and forwards
"""

## With annotations
## def function_name(pass: data_type) -> return_type
def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.

    """
    # backwards = string[::-1]
    # return backwards == string  # Returns either True or False
    return string[::-1].casefold() == string.casefold()  # Returns either True or False

word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

print("-" * 80)


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))

"""
************ functions that perform an action ************
"""

## Annotation using default values
def banner_text(text: str = " ", screen_width: int = 80) -> None:
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life")
banner_text("If life seems jolly rotten")
banner_text("There's something you've forgotten")
banner_text("And that's to laugh and smile and dance and sing")
banner_text()
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And...always look on the bright side of life...")
banner_text("*")

"""
Every Python functions returns something
Functions return None if you don't specify a value to return
"""

result_banner = banner_text("Nothing is returned")
print(result_banner)

"""
************ Fibonacci numbers ************
Each number is the sum of the two preceding numbers
"""

def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

"""
************ Printing in color ************
Note that this will not work on windows
Will need to install the colorama package for windows
1. download the colorama_lpa wheel
2. In IDE terminal cd to python project directory
3. pip install <path to wheel file>/colorama_lpa.version

1. File > Project Structure > SDK
"""

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences to change color, etc
    :param text: The text to print
    :param effect: The effect we want. One of the constants defined
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


color_print("Hello, Red", RED)
print("This should be in the default terminal color")
color_print("Hello, Blue", BLUE)
color_print("Hello, Yellow", YELLOW)
color_print("Hello, Bold", BOLD)
color_print("Hello, Underline", UNDERLINE)
color_print("Hello, Reverse", REVERSE)
color_print("Hello, Black", BLACK)



print(RED, "This will be red")
print("and so is this")

"""
************ Running your program like a user ************
right click python file on left pane > Open in > Terminal
pwd to get path
copy the path
open new terminal
cd <paste path you copied>
python3 --version
python3 <python_file_name>.py
Always test as a user before providing it to users
"""

"""
************ Activating a virtual environment ************
When you run a program, the first line it provides the path
Copy the first path - python path. Do not copy the python at the end
source /home/kevinstevens/Documents/Development/My_Python_Journey/venv/python/bin/activate
deactivate when finished
"""

## Testing our Hi-Low game with a function

LOW = 1
HIGH = 1000

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {} times, Max {} guesses"
      .format(correct_count, max_guesses))

"""
******** Fizz Buzz ********
"""

def fizz_buzz(number: int) -> str:
    """
    Play Fizz Buzz
    :param number: The number to check
    :return: 'fizz' if the number is divisible by 3
            'buzz' if it's divisible by 5
            'fizz buzz' if it's divisible by both 3 and 5
            The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

for i in range(1, 101):
    print(fizz_buzz(i))




