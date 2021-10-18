def is_palindrome(string: str):
    string = string.replace(" ", "").lower()
    result: bool = string == string[::-1]
    print(size)
    return result


def run():
    print(is_palindrome("1001"))


if __name__ == "__main__":
    run()
