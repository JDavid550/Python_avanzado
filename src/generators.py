
from tkinter import N


def my_gen():
    n = 0
    print(f'n = {n}')

    yield n

    n = 1
    print(f'n = {n}')

    yield n

    n = 2
    print(f'n = {n}')

    yield n

gen = my_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))