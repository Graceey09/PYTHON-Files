import unittest

from java_task_in_python.account import Account


class TestAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.grace = Account("Grace", "1", "1234")

    def test_deposit_method(self):
        self.grace.deposit(0)
        self.assertEqual(0, self.grace.check_balance("1234"))
        self.grace.deposit(500000)
        self.assertEqual(500000, self.grace.check_balance("1234"))

    def test_withdraw_method(self):
        self.grace.deposit(500000)
        self.assertEqual(500000, self.grace.check_balance("1234"))
        self.grace.withdraw(100000, "1234")
        self.assertEqual(400000, self.grace.check_balance("1234"))

    def test_validate_pin(self):
        self.grace.deposit(500000)
        self.assertEqual(500000, self.grace.check_balance("1234"))
        self.assertRaises(ValueError, self.grace.check_balance,"1235")

    def test_check_balance_method(self):
        self.grace.deposit(0)
        self.assertEqual(0, self.grace.check_balance("1234"))
        self.grace.deposit(500000)
        self.assertEqual(500000, self.grace.check_balance("1234"))

    def test_validate_withdrawal_method(self):
        self.grace.deposit(500000)
        self.assertEqual(500000, self.grace.check_balance("1234"))
        self.assertRaises(ValueError, self.grace.withdraw, -100000, "1234")
        self.assertEqual(500000, self.grace.check_balance("1234"))

    def test_can_update_pin(self):
        self.grace.deposit(500000)
        self.assertEqual(500000, self.grace.check_balance("1234"))
        self.grace.update_pin("1234","3456")
        self.grace.deposit(500000)
        self.assertEqual(1000000, self.grace.check_balance("3456"))


