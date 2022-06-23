from signal import raise_signal
from time import sleep


def nTermSum(a1,max):
    counter = 0
    a2 = a1 + 1
    n = 2

    while True:
        result = (n * (a1 + a2)) / 2
        if counter == max:
            raise StopIteration
        a2 += 1
        n += 1
        counter += 1

        yield result

if __name__ == '__main__':
    series = nTermSum(0,5)
    for i in series:
        print(i)
        sleep(1)

