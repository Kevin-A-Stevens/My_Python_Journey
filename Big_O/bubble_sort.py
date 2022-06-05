"""
In computer science, big O notation is used to classify algorithms
according to how their run time or space requirements grow as the
input size grows
"""


def bubble_sort(data: list) -> None:
    """Sorts a list in place"""
    n = len(data)
    comparison_count = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        print(f"End of pass {i}. 'data' is now {data}")
        if not swapped:
            # The last pass resulted in no swaps
            # The data is now sorted
            break

    print(f"Comparison_count is {comparison_count}")


# numbers = [3, 2, 4, 1, 5, 7, 6]
# numbers = [7, 6, 5, 4, 3, 2, 1]
# numbers = [1, 2, 3, 4, 6, 5, 7]
numbers = [1, 2, 3, 4, 5, 6, 7]

print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")


# x = 1
# y = 2
# print(x, y)
#
# x, y = y, x
# print(x, y)
