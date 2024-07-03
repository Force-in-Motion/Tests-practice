import pytest
from hw_3.src.average import average

data_test_positive = [([0, 2, 7, 9, 1], 3.8),
                      ([-4, -6, -2, -5], -4.25),
                      ([2.5, 4.8, 9.1, 5.5], 5.475),
                      ([-1.2, -4.2, -2.2, -9.2], -4.2),
                      ([0, -2.5, 8.5, -2.5], 0.875)]

@pytest.mark.aver_pos
@pytest.mark.parametrize('lst, result', data_test_positive)
def test_average_positive(lst, result):
    assert average(lst) == result

data_test_negative = [([], pytest.raises(ValueError)),
                      (12, pytest.raises(TypeError)),
                      ('str', pytest.raises(TypeError)),
                      (1.2, pytest.raises(TypeError)),
                      (True, pytest.raises(TypeError))]

@pytest.mark.aver_neg
@pytest.mark.parametrize('lst, result', data_test_negative)
def test_average_negative(lst, result):
    with result:
        assert average(lst) == result