import threading
import requests
import time
from multiprocessing import Pool


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


def cpu_bound_countdown(count: int):
    """
    Simple arithmetic CPU bound task to occupy the ALU
    :param count:
    """
    while count > 0:
        count -= 1


def io_bound_make_request(count: int):
    """
    IO Bound Tasks which asks a website for our IP Address
    :param count: how often we want to ask
    """
    for i in range(count):
        requests.get("https://httpbin.org/ip")


def single_threaded(function, count: int):
    """
    Runs a function with one thread
    :param function:  function to call
    :param count: size of countdown
    """
    multi_threaded(function, count, 1)


def multi_threaded(function, count: int, n_threads: int):
    """
    Runs a function with multiple threads dividing the workload evenly
    :param function:  function to call
    :param n_threads: number threads to create
    :param count: size of countdown
    """
    threads = [threading.Thread(target=function, args=[count // n_threads]) for _ in range(n_threads)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()


def multi_process(function, count: int, n_processes: int):
    """
    Runs a function with multiple processes dividing the workload evenly
    :param function:  function to call
    :param n_processes: number of processes to create
    :param count: size of countdown
    """
    pool = Pool(processes=n_processes)

    for _ in range(n_processes):
        pool.apply_async(function, [count // n_processes])

    pool.close()
    pool.join()


if __name__ == '__main__':

    print("\nMeasuring performance of CPU Bound tasks")
    counter = 200000000
    print(f"Counting from {counter} down to Zero")

    """ Single threaded execution for reference"""
    time_measurement(single_threaded, cpu_bound_countdown, counter)

    """ The Global Interpreter Lock GIL prevents multiple threads to run in parallel.
    Therefore multithreading for CPU bound tasks will perform worse than a single thread """
    time_measurement(multi_threaded, cpu_bound_countdown, counter, 8)

    """ Now with separate processes instead of threads, the GIL will not interfere anymore and we see a significant
    uplift in performance. Notice the uplift is not exactly a factor of how many processes will run since there is
    an overhead of copying all memory for all processes and spawning them"""
    time_measurement(multi_process, cpu_bound_countdown, counter, 8)

    print("\nMeasuring performance of IO Bound tasks\nGet current IP by calling https://httpbin.org/ip")
    counter = 8
    print(f"Asking for our IP {counter} times")

    """ Single threaded execution for reference"""
    time_measurement(single_threaded, io_bound_make_request, counter)

    """ The Global Interpreter Lock GIL prevents multiple threads to run in parallel.
    Therefore multithreading for CPU bound tasks will perform worse than a single thread """
    time_measurement(multi_threaded, io_bound_make_request, counter, 8)

    """ Now with separate processes instead of threads, the GIL will not interfere anymore and we see a significant
    uplift in performance. Notice the uplift is not exactly a factor of how many processes will run since there is
    an overhead of copying all memory for all processes and spawning them"""
    time_measurement(multi_process, io_bound_make_request, counter, 8)
