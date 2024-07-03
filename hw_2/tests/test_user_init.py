import pytest
from hw_2.src.user import User

data_test_positive = [('vasya', 15, User('vasya', 15)),
                      ('roma', 45, User('roma', 45)),
                      ('arkadiy', 89, User('arkadiy', 89)),
                      ('chuvak', 79, User('chuvak', 79))]

@pytest.mark.parametrize('name, age, result', data_test_positive)
def test_user_init(name, age, result):
    user = User(name, age)
    assert user.name == result.name and user.age == result.age


# data_test_negative = [(1, 0, pytest.raises(TypeError)),
#                       (12.7, 7, pytest.raises(TypeError)),
#                       (None, '', pytest.raises(TypeError)),
#                       (12, True, pytest.raises(TypeError)),
#                       (12, '', pytest.raises(TypeError)),
#                       (7.7, '', pytest.raises(TypeError)),
#                       (True, '', pytest.raises(TypeError))]
#
# @pytest.mark.parametrize('name, age, result', data_test_negative)
# def test_user_init_negative(name, age, result):
#     user = User(name, age)
#     with result:
#         assert user.name == ValueError or user.name == TypeError
#         assert user.age == ValueError or user.age == TypeError