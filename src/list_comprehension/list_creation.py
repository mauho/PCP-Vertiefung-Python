

def get_divisible_numbers_imp(divisor: int, maximum: int) -> list:
    """
    From the old days an imperative approach to generate a list containing all numbers of a series.
    :param divisor: by which a number must be divisible
    :param maximum: upper bound requested from the function
    :return: a list containing all number divisible by divisor
    """
    numbers = []
    for i in range(1, maximum + 1):
        if i % divisor == 0:
            numbers.append(i)

    return numbers


def get_divisible_numbers_func(divisor: int, maximum: int) -> list:
    """
    A more functional approach to generate a list containing all numbers of a series using list comprehension.
    :param divisor: by which a number must be divisible
    :param maximum: upper bound requested from the function
    :return: a list containing all number divisible by divisor
    """
    return [i for i in range(1, maximum + 1) if i % divisor == 0]


def main():
    print(get_divisible_numbers_imp(3, 100))
    print(get_divisible_numbers_func(3, 100))


if __name__ == '__main__':
    main()
