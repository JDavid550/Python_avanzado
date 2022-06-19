def base_func(func):
    
    
    def wrapper():
        print("Hello")
        func()
    
    return wrapper


@base_func
def parameter_func():
    print("This is the parameter function")

#parameter_func()

#base_func = base_func(parameter_func)

def run():
    #base_func()
    parameter_func()

if __name__ == '__main__':
    run()