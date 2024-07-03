import pytest
from hw_3.src.bankAccount import BankAccount

data_test_for_deposit_positive = [(2, 2),
                                  (2.8, 2.8),
                                  (9999999999999999999, 9999999999999999999)]

@pytest.mark.depos_pos
@pytest.mark.parametrize('val, result', data_test_for_deposit_positive)
def test_deposit_positive(val, result):
    bank = BankAccount(0)
    assert bank.deposit(val) is None
    assert bank.get_balance() == result


data_test_for_deposit_negative = [(-2, pytest.raises(ValueError)),
                                  (0, pytest.raises(ValueError)),
                                  ('0', pytest.raises(TypeError)),
                                  (bool, pytest.raises(TypeError)),
                                  (-2.7, pytest.raises(ValueError)),
                                  (None, pytest.raises(TypeError))]

@pytest.mark.depos_neg
@pytest.mark.parametrize('val, result', data_test_for_deposit_negative)
def test_deposit_negative(val, result):
    bank = BankAccount(0)
    with result:
        assert bank.deposit(val) is None
        assert bank.get_balance() == result


data_test_for_withdraw_positive = [(5, 45),
                                   (-7, 57),
                                   (0, 50),
                                   (7.2, 42.8),
                                   (-2.4, 52.4)]

@pytest.mark.withdraw_pos
@pytest.mark.parametrize('val, result', data_test_for_withdraw_positive)
def test_withdraw_positive(val, result):
    bank = BankAccount(50)
    assert bank.withdraw(val) is None
    assert bank.get_balance() == result


data_test_for_withdraw_negative = [('0', pytest.raises(TypeError)),
                                   (bool, pytest.raises(TypeError)),
                                   (None, pytest.raises(TypeError))]

@pytest.mark.withdraw_neg
@pytest.mark.parametrize('val, result', data_test_for_withdraw_negative)
def test_withdraw_negative(val, result):
    bank = BankAccount(50)
    with result:
        assert bank.withdraw(val) is None
        assert bank.get_balance() == result


data_test_get_balance = [(78789, 78789)]

@pytest.mark.get_balance
@pytest.mark.parametrize('val, result', data_test_get_balance)
def test_get_balance(val, result):
    bank = BankAccount(78789)
    assert bank.get_balance() == result