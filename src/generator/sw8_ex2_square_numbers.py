def number_producer(array, next_coroutine):
    """
        sends values from array to coroutine
        :param array: array with numbers to square
        :param next_coroutine: coroutine for sending values
        """
    for number in array:
        # send generated number to other coroutine
        next_coroutine.send(number)
    # stop the coroutine so it doesn't run indefinitely
    next_coroutine.close()


def squarer(next_coroutine):
    """
        squares received number
        :param next_coroutine: coroutine for sending values
        """
    try:
        while True:
            # receive value from other coroutine
            number = (yield)
            square_number = number ** 2
            # send number and square_number to other coroutine
            next_coroutine.send((number, square_number))

    except GeneratorExit:
        print("nothing more to squarer")


def print_number():
    """
        prints received values
        """
    try:
        while True:
            # receive values from other coroutine
            number, square_number = (yield)
            print("{}: {}".format(number, square_number))

    except GeneratorExit:
        print("nothing more to print")


# you have to start the coroutine with next() or send(None)
def main():
    printer = print_number()
    # printer.__next__()
    printer.send(None)
    square = squarer(printer)
    square.__next__()
    number_producer([1, 2, 3, 5, 8], square)


if __name__ == '__main__':
    main()

