from turtle import st


def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1] # This flips the word

def run():
    print(is_palindrome(1000))


if __name__ == "__main__":
    run()