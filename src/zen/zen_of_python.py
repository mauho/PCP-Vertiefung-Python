def print_zen():
    """
    Instead of printing each row in this class we live the zen of python by importing "this" which is an easter-egg
    that already does exactly what we want :-) which is - the zen of python
    """
    import this

    if this:
        pass


if __name__ == '__main__':
    print_zen()

