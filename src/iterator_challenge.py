from fibonacci_iterator import Fibonacci


palabra = "Hola"

letra = iter(palabra)

while True:
    try:
        print(next(letra))
    except StopIteration:
        break



class nTermsSum:

    def __init__(self, a1, max):
        self.a1 = a1
        self.a2 = a1+1
        self.max = max

    def __iter__(self):
        self.counter = 0
        self.n = 2 
        return self


    def __next__(self):
        self.result = (self.n * (self.a1 + self.a2)) / 2
        if self.counter == self.max:
            raise StopIteration
        self.a2 += 1
        self.n += 1 
        self.counter += 1

        return self.result

if __name__  == '__main__':

    series = nTermsSum(2,5)

    for i in series:
        print(i)