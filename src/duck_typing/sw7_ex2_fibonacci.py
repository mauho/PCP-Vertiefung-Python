def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_accumulator(n):
    def fib_acc(x, current, previous):
        if x == n:
            return current
        else:
            return fib_acc(x + 1, current + previous, current)

    return fib_acc(0, 0, 1)
