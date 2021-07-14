from unittest import TestCase

from bank_account import BankAccount


class TestBankAccount(TestCase):
    def setUp(self):
        self.bankaccount = BankAccount()


class TestGetBalance(TestBankAccount):
    def test_initial_balance(self):
        self.assertEqual(self.bankaccount.get_balance(), 0)
