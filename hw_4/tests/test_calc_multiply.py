import pytest
from hw_4.src.calculator import Calculator

data_test_positive = [(-7, -2, 14),
                      (89, 57, 5073),
                      (-24.5, -12.7, 311.15),
                      (24.7, 14.7, 363.09),
                      (-12.4, 45.4, -562.96),
                      (-47, 89, -4183),
                      (0, 0, 0),
                      (0, 67, 0),
                      (0, -59, 0),
                      (0, -47.8, 0),
                      (0, 89.4, 0)]

@pytest.mark.parametrize('val1, val2, result', data_test_positive)
def test_multiply_positive(val1, val2, result):
    calc = Calculator()
    assert calc.multiply(val1, val2) == result


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
                      (int, list, pytest.raises(TypeError))]

@pytest.mark.parametrize('val1, val2, result', data_test_negative)
def test_multiply_negative(val1, val2, result):
    calc = Calculator()
    with result:
        assert calc.multiply(val1, val2) == result