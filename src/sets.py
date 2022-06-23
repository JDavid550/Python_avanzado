my_set = {23, "Hello", True, (1,2)}
print(my_set)
print(type(my_set))

set1 = {}
set2 = set()

print(type(set1))
print(type(set2))

#We can turn a list into a set. This will get rid of repeated elements in the list.

my_list = [2, 2, 56, 6, 8, 9, 154]

my_list_turned_set = set(my_list)

my_list_turned_set.add(100)

my_list_turned_set.update([7,5], {36,665,1})

my_list_turned_set.discard(1)
my_list_turned_set.remove(2) #They do the same thing unless the element you're trying to delete doesn't exist. In that case remove throws an erro while discard only keeps the set the same way

my_list_turned_set.pop() #Deletes a random element
my_list_turned_set.clear() # Clear up the whole set

print(my_list_turned_set)
