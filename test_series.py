"""This file test code for series.py."""


import pytest

# def test_fibonacci():
#     from series import fibonacci
#     assert fibonacci(5) == 5

def test_lucas():
    from series import lucas
    assert lucas(5) == 11
