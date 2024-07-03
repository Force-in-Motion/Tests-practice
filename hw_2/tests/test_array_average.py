import pytest
from hw_2.src.array import Array

data_test_positive = [([-7, -2, -4, -8], -5.25),
                      ([9, 5, 8, 8], 7.5),
                      ([-4.2, -2.2, -5.2, -8.2], -4.95),
                      ([4.7, 1.7, 7.5, 4.8], 4.675),
                      ([-2.4, 5.4, -7.2, 8.2], 1.0),
                      ([-7, 9, 8, -5], 1.25),
                      ([0, 0, 0, 0], 0.0),
                      ([0, -7, 0, -9], -4.0),
                      ([0, 9, 8, 0], 4.25),
                      ([0, 4.8, 0, 8.8], 3.4000000000000004),
                      ([0, -7.8, 0, -5.8], -3.4)]

@pytest.mark.parametrize('lst, result', data_test_positive)
def test_array_average_positive(lst, result):
    arr = Array(*lst)
    assert arr.average() == result

data_test_negative = [([None, None, 'str', True], pytest.raises(TypeError)),
                      ([None,'str', 7, 5.5], pytest.raises(TypeError)),
                      ([None, True, 8, 'str'], pytest.raises(TypeError)),
                      ([None, 8, 5.5, 'str'], pytest.raises(TypeError)),
                      ([None, 5.5, True, 'str'], pytest.raises(TypeError)),
                      ([[5, 2], 5.5, 'str', 5.5], pytest.raises(TypeError)),
                      (['str', 5.5, 8, 5.7], pytest.raises(TypeError))]

@pytest.mark.parametrize('lst, result', data_test_negative)
def test_array_average_negative(lst, result):
    arr = Array(*lst)
    with result:
        assert arr.average() == result