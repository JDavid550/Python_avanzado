## Generate a script that generates a random list of numbers and return a dictionary with mean, median and standard variation 
# Random list
# Calculate parameters
# Create decorator to generate the dictionary from those values
from typing import Callable, Dict, List
import numpy as np
import random



def generate_list() -> List[int]:
    numbers_set: int = int(input('How much numbers do you want in your list?: '))
    list: List[int] = random.sample(range(1000), numbers_set)
    print(f'This is the generated list {list}')
    return list


list: List[int] = generate_list()
parameters: List[str] = ['mean', 'median', 'std']

#Decorator
def create_dictionary(func) -> Callable:
    def wrapper() -> Dict[str, int]:
        results = func(list)
        dictionary: Dict[str, int]  = dict(zip(parameters, results))
        print(dictionary)
        return dictionary
    return wrapper


@create_dictionary
def calculate_parameters(list) -> List[float]:
    mean: float = round(np.mean(list))
    median: float = round(np.median(list))
    std: float = round(np.std(list),2)
    print(f'This are the results {mean, median, std}')
    return [mean, median, std]


def run():
    calculate_parameters()


if __name__ == '__main__':
    run()