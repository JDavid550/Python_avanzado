from datetime import date, datetime

def execution_time(func):
    def wrapper(*args, **kwargs): #args and kwargs allows to receive any parameters in the wrapper nested function
        initial_time = datetime.now()
        func(*args, **kwargs) #it must be placed here as well
        final_time = datetime.now()
        time_elapsed = final_time-initial_time
        print (f'Its been {time_elapsed.total_seconds()} seconds of execution')
    return wrapper

@execution_time
def random_func():
    for i in range(1, 1000000):
        pass

@execution_time
def sum(a: int,b: int)-> int:
    return a + b

random_func()
sum(2,6)

