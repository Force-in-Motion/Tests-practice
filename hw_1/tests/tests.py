import pytest
from hw_1.src.main import average
from hw_1.src.main import factorial

data_test1 = [([], ValueError),
             ([5], 5),
             ([i for i in range(10000)], 4999.5),
             ([3, 1, 4, 1, 5], 2.8),
             ([-1, -3, -2, -4], -2.5),
             ([2, -1, 3, -5, 0], -0.2),
             ((bool, str, float, int, None), TypeError),
             ([0, 0, 0, 0, 0, 0, 0], 0)]

@pytest.mark.parametrize("value1, result1", data_test1)
def test_average(value1, result1):

    assert average(value1) == result1

data_test2 = [(True, TypeError),
             ('ananas', TypeError),
             (127.8, TypeError),
             (8, 40320),
             (None, TypeError),
             (0, 1),
             (-78, ValueError),
             (7, 5040)]


@pytest.mark.parametrize('value2, result2', data_test2)
def test_factorial(value2, result2):

    assert factorial(value2) == result2