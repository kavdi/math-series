"""This file contains fuctions to create fibonacci series and lucas numbers."""


def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) <= n:
        last_fib = fib_list[len(fib_list) - 1]
        sib_fib = fib_list[len(fib_list) - 2]
        fib_list.append(last_fib + sib_fib)
    return fib_list.pop()


# def lucas(n):


# def sum_series(a, b):