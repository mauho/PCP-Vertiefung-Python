
def fib_generator(end):
    a = 0
    b = 1
    while a < end:
        yield a
        a, b = b, a + b


def main():
    for number in fib_generator(10):
        print(number)

    demo_list = [67, 2, 4, 10]
    generator = (x ** 2 for x in demo_list)
    print(generator.__next__())


if __name__ == '__main__':
    main()
