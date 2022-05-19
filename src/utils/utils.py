import time


def time_measurement(function, *args) -> float:
    """
    Takes a function and args. Returns the result of the function (if any) and prints the duration of the execution.
    :param function: Function to execute
    :param args: Parameters to pass to the function
    :return: Result of executed function
    """
    start = time.time()
    result = function(*args)
    end = time.time()
    print(f'{function.__name__} took {"%.2f" % (end - start)} seconds')
    return result
