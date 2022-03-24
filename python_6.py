"""
************ Functions ************
A function that is bound to an instance of a class is called a Method
"""

"""
************ Defining a function ************
"""


def multiply(x, y):
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

def banner_text(text, screen_width):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*", 66)
banner_text("Always look on the bright side of life", 66)
banner_text("If life seems jolly rotten", 66)
banner_text("There's something you've forgotten", 66)
banner_text("And that's to laugh and smile and dance and sing", 66)
banner_text(" ", 66)
banner_text("When you're feeling in the dumps,", 66)
banner_text("Don't be silly chumps,", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And...always look on the bright side of life...", 66)
banner_text("*", 66)

"""
Every Python functions returns something
Functions return None if you don't specify a value to return
"""

result = banner_text("Nothing is returned", 66)
print(result)

