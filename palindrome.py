def is_palindrome(string: str, size: dict[tuple[str, int]]):
    string = string.replace(" ", "").lower()
    result: bool = string == string[::-1]
    print(size)
    return result


def run():
    print(is_palindrome("1001", [{"Hola": 1}, {"hey": 1}]))


if __name__ == "__main__":
    run()
