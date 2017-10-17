"""This file test code for series.py."""


import pytest

def test_fibonacci(n):
"""Testing for fibonacci sequence and lucas"""
    if len(fib_list) == n and fib_list[n-1] == (fib_list[n-2] + fib_list[n-3]):
        return True
    else:
        return False