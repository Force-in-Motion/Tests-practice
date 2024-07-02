import pytest
from hw_4.src.user import User

data_test_positive = [('Leonard', 17, 18),
                      ('Sasay', 27, 28),
                      ('Georg', 37, 38),
                      ('Kashtan', 77, 78),
                      ('Ukrop', 97, 98)]

@pytest.mark.parametrize('name, age, result', data_test_positive)
def test_user_up_age_positive(name, age, result):
    user = User(name, age)
    assert user.up_age() == result