## Generate a script that generates a random list of numbers and return a dictionary with mean, median and standard variation 
# Random list
# Calculate parameters
# Create decorator to generate the dictionary from those values
from ast import arg
from unittest import result
import numpy as np
import random



def generate_list():
    numbers_set = int(input('How much numbers do you want in your list?: '))
    list = random.sample(range(1000), numbers_set)
    print(list)
    return list


list = generate_list()
parameters = ['mean', 'median', 'std']

def calculate_parameters(list):
    mean = np.mean(list)
    median = np.median(list)
    std = round(np.std(list),2)
    print(mean, median, std)
    return [mean, median, std]


def create_dictionary():
    results = calculate_parameters(list)
    print(results)
    dictionary  = dict(zip(parameters, results))
    print(dictionary)
    return results


def run():
    create_dictionary()


if __name__ == '__main__':
    run()