from typing import Callable


def print_strings(string: str)-> Callable:

    def multiply(n: int):
        assert type(string) == str, 'This is not an string'
        return string * n

    return multiply


times5 = print_strings("Hola ")

print(times5(5))

prueba = print_strings("prueba ")(5)

print(prueba)