def fibonacci():
    current, previous = 0, 1
    while True:
        current, previous = current + previous, current
        yield current

"""
Return sends a specified value back to its caller whereas Yield 
can produce a sequence of values. We should use yield when we 
want to iterate over a sequence, but don’t want to store the 
entire sequence in memory.

Yield are used in Python generators. A generator function is 
defined like a normal function, but whenever it needs to 
generate a value, it does so with the yield keyword rather 
than return. If the body of a def contains yield, the function 
automatically becomes a generator function.
"""

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))