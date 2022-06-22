## for loop in Python is actually syntax sugar 


from unittest import result


list = [1,2,3,4,5]
my_iter = iter(list)

print(next(my_iter))

#This is how a for loop works internally
while True:
    try:
        item = next(my_iter)
        print(item)
    except StopIteration:
        break

##Example of an iterator for a loop of EvenNumbers

class EvenNumbers:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


for i in EvenNumbers(6):
    print(i)