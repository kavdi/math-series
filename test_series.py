"""This file test code for series.py."""


import pytest

def test_fibonacci():
    from series import fibonacci
    assert fibonacci(5) == 5
    #assert len(fib_list) == n and fib_list[n-1] == (fib_list[n-2] + fib_list[n-3])
