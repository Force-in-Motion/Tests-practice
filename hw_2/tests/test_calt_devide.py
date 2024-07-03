import pytest
from hw_2.src.calculator import Calculator

data_test_positive = [(-7, -2, 3.5),
                      (950, 2, 475),
                      (-240.5, -4, 60.125),
                      (240.5, 3.7, 65),
                      (-12.4, 4, -3.1),
                      (-470, 5, -94)]

@pytest.mark.parametrize('val1, val2, result', data_test_positive)
def test_divide_positive(val1, val2, result):
    calc = Calculator()
    assert calc.divide(val1, val2) == result

data_test_negative = [(None, None, pytest.raises(TypeError)),
                      (None, str, pytest.raises(TypeError)),
                      (None, bool, pytest.raises(TypeError)),
                      (None, int, pytest.raises(TypeError)),
                      (None, float, pytest.raises(TypeError)),
                      (None, list, pytest.raises(TypeError)),
                      (str, int, pytest.raises(TypeError)),
                      (str, float, pytest.raises(TypeError)),
                      (str, str, pytest.raises(TypeError)),
                      (str, list, pytest.raises(TypeError)),
                      (bool, int, pytest.raises(TypeError)),
                      (bool, float, pytest.raises(TypeError)),
                      (bool, list, pytest.raises(TypeError)),
                      (int, list, pytest.raises(TypeError)),
                      (0, 0, pytest.raises(ZeroDivisionError)),
                      (78, 0, pytest.raises(ZeroDivisionError))]

@pytest.mark.parametrize('val1, val2, result', data_test_negative)
def test_divide_negative(val1, val2, result):
    calc = Calculator()
    with result:
        assert calc.divide(val1, val2) == result