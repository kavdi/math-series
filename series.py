"""This file contains fuctions to create fibonacci series and lucas numbers."""


# def fibonacci(n):
#     fib_list = [0, 1]
#     while len(fib_list) <= n:
#         last_fib = fib_list[len(fib_list) - 1]
#         sib_fib = fib_list[len(fib_list) - 2]
#         fib_list.append(last_fib + sib_fib)
#     return fib_list.pop()


def lucas(n):
    luc_list = [2, 1]
    while len(luc_list) <= n:
        last_luc = luc_list[len(luc_list) - 1]
        sib_luc = luc_list[len(luc_list) - 2]
        luc_list.append(last_luc + sib_luc)
    return luc_list.pop()

# def sum_series(a, b):