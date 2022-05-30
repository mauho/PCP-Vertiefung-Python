def fib(n):
    """
        returns value of searched fibonacci number
        :param n: searched fibonacci number
        """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_accumulator(n):
    """
        returns value of searched fibonacci number
        :param n: searched fibonacci number
        """
    def fib_acc(x, current, previous):
        if x == n:
            return current
        else:
            return fib_acc(x + 1, current + previous, current)

    return fib_acc(0, 0, 1)
