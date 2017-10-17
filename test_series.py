"""This file test code for series.py."""


import pytest


FIB_PARAMS = [(2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)]


LUC_PARAMS = [(2, 3), (3, 4), (4, 7), (5, 11), (6, 18), (7, 29)]


SUM_PARAMS = [(2, 0, 1, 1), (3, 0, 1, 2), (4, 0, 1, 3), (5, 0, 1, 5), (6, 0, 1, 8), (7, 0, 1, 13), (2, 2, 1, 3), (3, 2, 1, 4), (4, 2, 1, 7), (5, 2, 1, 11), (6, 2, 1, 18), (7, 2, 1, 29)]


@pytest.mark.parametrize('n, result', FIB_PARAMS)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUC_PARAMS)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, a, b, result', SUM_PARAMS)
def test_sum_series(n, a, b, result):
    from series import sum_series
    assert sum_series(n, a, b)  == result
