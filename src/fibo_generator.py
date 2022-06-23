from time import sleep

#Fibonacci generator:

def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if aux > max:
                raise StopIteration
            n1, n2= n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    fibo = fibo_gen(5)
    for i in fibo:
        print(i)
        sleep(1)