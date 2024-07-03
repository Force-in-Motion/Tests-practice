import pytest
from hw_3.src.palindrome import is_palindrome

data_test_positive = [('assa', True),
                      ('sdfsf', False),
                      ('awaawa', True),
                      ('sdsdf', False)]
@pytest.mark.pal_pos
@pytest.mark.parametrize('val, result', data_test_positive)
def test_palindrome_positive(val, result):
    assert is_palindrome(val) == result

data_test_negative = [('', pytest.raises(ValueError)),
                      (12, pytest.raises(TypeError)),
                      (None, pytest.raises(TypeError)),
                      (4.7, pytest.raises(TypeError)),
                      (True, pytest.raises(TypeError))]

@pytest.mark.pal_neg
@pytest.mark.parametrize('val, result', data_test_negative)
def test_palindrome_negative(val, result):
    with result:
        assert is_palindrome(val) == result

