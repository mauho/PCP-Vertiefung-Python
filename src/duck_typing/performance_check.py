import time
from src.duck_typing.sw7_ex2_fibonacci import fib


# from src.concurrency.threads_vs_processes import time_measurement


# not able to run in terminal if function is imported
def time_measurement(function, param):
    """
    Takes a function and a parameter. Returns the result of the function and prints the duration of the execution.
    :param function: Function to execute
    :param param: Parameter to pass
    :return: Result of executed function
    """
    start = time.time()
    result = function(param)
    end = time.time()
    print(f'{function.__name__} took {"%.2f" % (end - start)} seconds')
    return result


def main():
    print(time_measurement(fib, 38))


if __name__ == '__main__':
    main()

# run in project folder
# pypy3 -m src.duck_typing.performance_check
# with pypy3 it takes 1s to run code

# python3 -m src.duck_typing.performance_check
# with python3 it takes 15s to run code
