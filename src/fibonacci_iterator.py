from time import sleep

class Fibonacci:
    def __init__(self, max): #It's created when a new class is instanced
        self.max = max


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if self.aux  > self.max:
                raise StopIteration
            #self.n1  = self.n2
            ##self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux #Utilizando el swapping para esto
            self.counter += 1
            return self.aux


if __name__ == '__main__':
    fibonacci = Fibonacci(5)
    for i in fibonacci:
        print(i)
        sleep(1)