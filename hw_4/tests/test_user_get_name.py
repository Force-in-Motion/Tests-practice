import pytest
from hw_4.src.user import User

data_test_positive = [(User('Leonard', 17), 'Leonard'),
                      (User('Sasay', 27), 'Sasay'),
                      (User('Georg', 17), 'Georg'),
                      (User('Kashtan', 17), 'Kashtan'),
                      (User('Ukrop', 17), 'Ukrop')]

@pytest.mark.parametrize('user, result', data_test_positive)
def test_user_get_name_positive(user, result):
    assert user.get_name() == result