"""
************ Functions ************
A function that is bound to an instance of a class is called a Method
"""

"""
************ Defining a function ************
"""


def multiply(x, y):
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

def is_palindrome(string):
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


def palindrome_sentence(sentence):
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

def banner_text(text=" ", screen_width=80):
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

def fibonacci(n):
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
