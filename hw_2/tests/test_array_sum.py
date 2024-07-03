import pytest
from hw_2.src.array import Array

data_test_positive = [([-7, -2, -4, -8], -21),
                      ([89, 57, 89, 58], 293),
                      ([-24.5, -12.7, -45.7, -78.2], -161.10000000000002),
                      ([24.7, 14.7, 57.5, 24.8], 121.7),
                      ([-12.4, 45.4, -57.2, 78.9], 54.7),
                      ([-47, 89, 78, -58], 62),
                      ([0, 0, 0, 0], 0),
                      ([0, -67, 0, -89], -156),
                      ([0, 59, 89, 0], 148),
                      ([0, 47.8, 0, 58.8], 106.6),
                      ([0, -47.8, 0, -58.8], -106.6)]

@pytest.mark.parametrize('lst, result', data_test_positive)
def test_array_sum_positive(lst, result):
    arr = Array(*lst)
    assert arr.sum() == result

data_test_negative = [([None, None, 'str', True], pytest.raises(TypeError)),
                      ([None,'str', 7, 5.5], pytest.raises(TypeError)),
                      ([None, True, 8, 'str'], pytest.raises(TypeError)),
                      ([None, 8, 5.5, 'str'], pytest.raises(TypeError)),
                      ([None, 5.5, True, 'str'], pytest.raises(TypeError)),
                      ([[5, 2], 5.5, 'str', 5.5], pytest.raises(TypeError)),
                      (['str', 5.5, 8, 5.7], pytest.raises(TypeError))]


