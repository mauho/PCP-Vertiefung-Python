import time


def time_measurement(function, param) -> float:
    """
    Takes a function and a parameter. Returns the result of the function and prints the duration of the execution.
    :param function: Function to execute
    :param param: Parameter to pass
    :return: Result of executed function
    """
    start = time.time()
    result = function(param)
    end = time.time()
    print(f'{function.__name__} took {"%.2f" % (end-start)} seconds')
    return result


if __name__ == '__main__':
    print(time_measurement(sum, range(100000001)))
