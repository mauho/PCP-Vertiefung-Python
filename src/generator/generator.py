
def fib_generator(end):
    """
    creates a sequence of fibonacci numbers
    :param end: the last fibonacci number we want
    """
    a = 0
    b = 1
    while a < end:
        yield a
        a, b = b, a + b


def squares_generator(length):
    """
        squares numbers in a range from 0 to length
        :param length: end of range from 0
        """
    for n in range(length):
        yield n ** 2


def main():
    for number in fib_generator(10):
        print(number)

    long_form_generator = squares_generator(6)
    print(long_form_generator.__next__())

    # This is a generator expression, a shorter version of the squares_generator()
    generator = (n ** 2 for n in range(6))
    print(generator.__next__())


if __name__ == '__main__':
    main()
