z= 5

def func():
    z = 3
    
    def other_func():
        z = 2

        print(z)
    
    other_func()

    print(z)

func()

print(z)