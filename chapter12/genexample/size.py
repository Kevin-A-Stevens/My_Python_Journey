import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start  # returns yielded value then suspends
        start += 1

# _ = input("line 12")
# big_range = range(10000)
# big_range = my_range(10000)S
big_range = my_range(5)
# _ = input("line 16")

# print("big_range is {} bytes".format(sys.getsizeof(big_range)))  # 48
# print("big_range is {} bytes".format(sys.getsizeof(big_range)))  # 112
print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range

big_list = []
# _ = input("line 25")
for val in big_range:
    # _ = input("line 27 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))  # 87616
print(big_range)
print(big_list)

print("Looping again ... or not")
for i in my_range(5):
    print("i is {}".format(i))



