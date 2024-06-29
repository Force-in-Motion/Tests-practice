import pytest
from hw_4.src.calculator import Calculator

data_test = [(-2, -7, -9),
             (57, 89, 146),
             (-24.5, -12.7, -37.2),
             (24.7, 14.7, 39.4),
             (-12.4, 45.4, 33),
             (-47, 89, 42),
             (0, 0, 0),
             (0, 67, 67),
             (0, -59, -59),
             (0, -47.8, -47.8),
             (0, 89.4, 89.4)]

@pytest.mark.parametrize('val1, val2, result', data_test)
def test_add_positive(val1, val2, result):
    calc = Calculator()
    assert calc.add(val1, val2) == result
