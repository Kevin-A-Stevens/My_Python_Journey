def print_backwards(*args, **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open("backwards.txt", "w") as backwards:
    print_backwards("Hello", "world", "earth", file=backwards)



