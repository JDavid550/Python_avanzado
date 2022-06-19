def main():

    x = 1

    def func():
        print(x)
    
    return func

my_func = main()
my_func()

del(main)

my_func() ## This is what prints the second 1, due to it saves the context of the nested function


def multiplier(x):

    def multiply(n):
        return x * n

    return multiply

times5 = multiplier(5)
times10 = multiplier(10)

print(times5(6))
print(times10(2))
print(times10(times5(3)))