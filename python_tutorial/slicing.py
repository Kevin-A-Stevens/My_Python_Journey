digits = [0,1,2,3,4,5,6,7,8,9]

print(digits[0])  # 0
print(digits[-1])  # 9
print(digits[-len(digits)])  # 0
print(digits[0:3])  # [0, 1, 2]
print(digits[:3])  # [0, 1, 2]

name = "First Last"
print(name[:5])  # First
print(digits[0:-1])  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(digits[5:])  # [5, 6, 7, 8, 9]
print(digits[:10:2])  # [0, 2, 4, 6, 8]
print(digits[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Try to always use the len function in a loop
for i in range(len(digits)):
    print(digits[:i])

print()

window_size = 7
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])






