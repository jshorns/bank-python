import pytest

from bank.bank_account import BankAccount


@pytest.fixture
def bank_account():
    return BankAccount()


def test_get_balance(bank_account):
    assert bank_account.get_balance() == 0
