import pytest
from hw_2.src.user import User

data_test_positive = [(User('Leonard', 17), 17),
                      (User('Sasay', 27), 27),
                      (User('Georg', 37), 37),
                      (User('Kashtan', 77), 77),
                      (User('Ukrop', 97), 97)]

@pytest.mark.parametrize('user, result', data_test_positive)
def test_user_get_age_positive(user, result):
    assert user.get_age() == result