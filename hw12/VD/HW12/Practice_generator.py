"""Create a simple generator function similar to the range iterator.
"""

def generator(start=0, stop=1, step=1):
    while start != stop:
        yield start
        start += step

my = generator(0, 10, 0.5)
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))