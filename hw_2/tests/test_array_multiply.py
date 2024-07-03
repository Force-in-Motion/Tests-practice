import pytest
from hw_2.src.array import Array

data_test_positive = [([-7, -2, -4, -8], 448),
                      ([9, 5, 8, 8], 2880),
                      ([-4.5, -12.7, -5.7, -8.2], 2671.191),
                      ([4.7, 1.7, 7.5, 4.8], 287.64),
                      ([-12.4, 5.4, -7.2, 8.2], 3953.3184),
                      ([-7, 9, 8, -5], 2520),
                      ([0, 0, 0, 0], 0),
                      ([0, -7, 0, -9], 0),
                      ([0, 9, 8, 0], 0),
                      ([0, 4.8, 0, 8.8], 0),
                      ([0, -7.8, 0, -5.8], 0)]

@pytest.mark.parametrize('lst, result', data_test_positive)
def test_array_multiply_positive(lst, result):
    arr = Array(*lst)
    assert arr.multiply() == result

data_test_negative = [([None, None, 'str', True], pytest.raises(TypeError)),
                      ([None,'str', 7, 5.5], pytest.raises(TypeError)),
                      ([None, True, 8, 'str'], pytest.raises(TypeError)),
                      ([None, 8, 5.5, 'str'], pytest.raises(TypeError)),
                      ([None, 5.5, True, 'str'], pytest.raises(TypeError)),
                      ([[5, 2], 5.5, 'str', 5.5], pytest.raises(TypeError)),
                      (['str', 5.5, 8, 5.7], pytest.raises(TypeError))]

@pytest.mark.parametrize('lst, result', data_test_negative)
def test_array_multiply_negative(lst, result):
    arr = Array(*lst)
    with result:
        assert arr.multiply() == result