from typing import List


my_set1 = {1,2,3,4}
my_set2 = {3,7,0,8}

join_set = my_set1 | my_set2
inner_set = my_set1 & my_set2
asymetric_difference1 = my_set1 - my_set2
asymetric_difference2 = my_set2 - my_set1 #It's keeping the elements that are not contained by both sets

simetric_difference =  my_set1 ^ my_set2 #It's keeping the elements that are not repeated in both sets

my_set1.union(my_set2)
my_set1.symmetric_difference(my_set2)
my_set1.difference(my_set2)
my_set1.intersection(my_set2)

print(join_set)
print(inner_set)
print(asymetric_difference1)
print(asymetric_difference2)
print(simetric_difference)

my_list = [2,2,2,2,2,23]
def remove_repeated(list):
    without_repeated_list = []
    for element in list:
        if element not in without_repeated_list:
            without_repeated_list.append(element)
    
    return without_repeated_list

print(remove_repeated(my_list))

def remove_repeated_with_sets(my_list) -> List[int]:
    without_repeated_list: set = set(my_list)
    return list(without_repeated_list)

print(remove_repeated_with_sets(my_list))


    