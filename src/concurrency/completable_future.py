import time

from concurrent.futures import ThreadPoolExecutor

half_second = 500
two_seconds = 2000
three_seconds = 3000
six_seconds = 6000


def do_blocking_wait(milis: float):
    time.sleep(0.001 * milis)


def long_lasting_task() -> float:
    do_blocking_wait(three_seconds)
    print(str(three_seconds), end='')
    return three_seconds


def even_longer_lasting_task() -> float:
    do_blocking_wait(six_seconds)
    print(str(six_seconds), end='')
    return six_seconds


def last_task_future(a, b):
    s = a.result()
    t = b.result()
    do_blocking_wait(two_seconds)
    return str("was waiting for " + str(s + t + two_seconds) + "ms")


def main():
    start = time.time()

    executor = ThreadPoolExecutor(max_workers=3)
    a = executor.submit(long_lasting_task)
    b = executor.submit(even_longer_lasting_task)
    c = executor.submit(last_task_future, a, b)

    print("\n-> Now waiting for things to happen!")

    while not c.done():
        print(".", end='')
        time.sleep(0.001 * half_second)

    print(c.result())
    print(f"-> Done. This took {'%.2f' % (time.time() - start)} seconds ")


if __name__ == '__main__':
    main()
