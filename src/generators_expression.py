from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): #args and kwargs allows to receive any parameters in the wrapper nested function
        initial_time = datetime.now()
        func(*args, **kwargs) #it must be placed here as well
        final_time = datetime.now()
        time_elapsed = final_time-initial_time
        print (f'Its been {time_elapsed.total_seconds()} seconds of execution')
    return wrapper

list = [1,2,3,4,5,6,7,8,9]

@execution_time
def generate_list_comprehenssion():
    sqrt_list = [pow(x,3) for x in list]
    print(sqrt_list)
    return sqrt_list

@execution_time
def generate_list_gen_comprehenssion():
    sqrt_list = (pow(x,3) for x in list) # This creates an object that  when it's called returns the latest yield
    for i in sqrt_list:
        print(i)
    return sqrt_list

generate_list_comprehenssion()
gen = generate_list_gen_comprehenssion() #Using the generator comprehenssion is faster than using list comprehenssion. This is useful in case of large amount of data.

""" print(next(gen))
print(next(gen))
print(next(gen)) """ # it's necesary to remove the decorator from the function to print each one
