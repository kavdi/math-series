"""This file contains fuctions to create fibonacci series and lucas numbers."""


def fibonacci(n):
    """Create the fibonacci sequence and returns nth value."""
    fib_list = [0, 1]
    while len(fib_list) <= n:
        last_fib = fib_list[len(fib_list) - 1]
        sib_fib = fib_list[len(fib_list) - 2]
        fib_list.append(last_fib + sib_fib)
    return fib_list.pop()


def lucas(n):
    """Create the lucas numbers and return the nth value."""
    luc_list = [2, 1]
    while len(luc_list) <= n:
        last_luc = luc_list[len(luc_list) - 1]
        sib_luc = luc_list[len(luc_list) - 2]
        luc_list.append(last_luc + sib_luc)
    return luc_list.pop()


def sum_series(n, a=0, b=1):
    """Take in 3 arguments and returns nth value of either.

    The fibonacci sequence, lucas numbers or random sequence.
    """
    final_list = [a, b]
    while len(final_list) <= n:
        last_final = final_list[len(final_list) - 1]
        sib_final = final_list[len(final_list) - 2]
        final_list.append(last_final + sib_final)
    return final_list.pop()


if __name__ == '__main__':
    print(__doc__)
    print(" ")
    print("fibonacci(4):", fibonacci(4))
    print(fibonacci.__doc__)
    print(" ")
    print("lucas(4):", lucas(4))
    print(lucas.__doc__)
    print(" ")
    print("sum_series(4):", sum_series(4))
    print(sum_series.__doc__)
