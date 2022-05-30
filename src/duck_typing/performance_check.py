from src.duck_typing.sw7_ex2_fibonacci import fib
from src.utils.utils import time_measurement


def main():
    print(time_measurement(fib, 38))


if __name__ == '__main__':
    main()

# run in project folder
# pypy3 -m src.duck_typing.performance_check
# with pypy3 it takes 1s to run code

# python3 -m src.duck_typing.performance_check
# with python3 it takes 15s to run code
