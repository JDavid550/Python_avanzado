def is_prime(number: int) -> bool:
    counter: int = 0
    for i in range(1, number+1):
        if i == number or i == 1:
            print(f'Counter first if: {counter}')
            continue
        if number % i == 0:
            counter += 1
            print(f'Counter second if: {counter}')
    if counter == 0:
        return True
    else:
        return False


def run():
    if is_prime(5):
        print('Its prime')
    else:
        print('Its not prime')


if __name__ == '__main__':
    run()