def division(n: int):
    def division_1(x: int):
        return n / x

    return division_1


def run():
    divider = division(5)
    print(divider(2))


if __name__ == "__main__":
    run()
