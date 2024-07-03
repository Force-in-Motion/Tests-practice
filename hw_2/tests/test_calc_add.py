import pytest
from hw_2.src.calculator import Calculator

data_test_positive = [(-2, -7, -9),
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

@pytest.mark.parametrize('val1, val2, result', data_test_positive)
def test_add_positive(val1, val2, result):
    calc = Calculator()
    assert calc.add(val1, val2) == result


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
def test_add_negative(val1, val2, result):
    calc = Calculator()
    with result:
        assert calc.add(val1, val2) == result