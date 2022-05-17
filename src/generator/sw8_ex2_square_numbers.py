
def number_producer(array, next_coroutine):
    for number in array:
        next_coroutine.send(number)
    next_coroutine.close()


def squarer(next_coroutine):
    try:
        while True:
            number = (yield)
            square_number = number ** 2
            next_coroutine.send((number, square_number))

    except GeneratorExit:
        print("nothing more to squarer")


def print_number():
    try:
        while True:
            number, square_number = (yield)
            print("{}: {}".format(number, square_number))

    except GeneratorExit:
        print("nothing more to print")


def main():
    printer = print_number()
    printer.__next__()
    square = squarer(printer)
    square.__next__()
    number_producer([1, 2, 3, 5, 8], square)


if __name__ == '__main__':
    main()

