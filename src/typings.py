from typing import Dict, List, Tuple

print("Hello world")

DEFUALT_PHONE = "21654695"


def get_phone():
    phone: int = input("Give me your phone: ") # The type int after variable's name allows to define the variable as a single type
    if not phone:
        phone = DEFUALT_PHONE.round() # This will throw an error
    
    return int(phone)

a = 3
b = 2


def sum(a:int, b: int) -> int:
    return a + b

positives: List[int] = [1,2,3,4]

users: Dict[str, str] = {
    "Name": "Pepe"
}

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = 3

def run():
    my_phone = get_phone()
    print(f'Your phone is {my_phone}')
    print(sum(a,b))
    print(positives, users)
    print(coordinates)

run()

