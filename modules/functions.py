def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=" "):
    text = ""  # In case a number is entered for text
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text # indicates the string is returned


with open("menu", mode="w") as menu:
    # Call the function
    # All python functions return something
    # If we do not specify then the function returns None

    s1 = center_text("Spam and eggs")
    print(s1, file=menu)
    s2 = center_text("Ham, spam and eggs")
    print(s2, file=menu)
    s3 = center_text(12)
    print(s3, file=menu)
    s4 = center_text("Spam, spam, and spam")
    print(s4, file=menu)
    s5 = center_text("First", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)

python_food()




