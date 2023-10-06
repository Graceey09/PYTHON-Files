import unittest

from java_task_in_python.bank_app import Bank


class TestBankFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank("BANK OF GRACE")
        self.bank.register("Grace", "Maduekwe", "1234")

    def test_that_can_register_customer(self):
        self.bank.register("Grace", "Maduekwe", "1234")
        self.assertEqual("Grace Maduekwe", self.bank.find_account("1").get_name())

    def test_deposit_method(self):
        self.bank.deposit("1", 10_000)
        self.assertEqual(10_000, self.bank.check_balance("1", "1234"))

    def test_withdrawal(self):
        self.bank.deposit("1", 10_000)
        self.assertEqual(10_000, self.bank.check_balance("1", "1234"))
        self.bank.withdraw("1", 5_000, "1234")
        self.assertEqual(5_000, self.bank.check_balance("1", "1234"))

    def test_transfer_method(self):
        self.bank.register("Precious", "Raphael", "1234")
        self.assertEqual("Precious Raphael", self.bank.find_account("2").get_name())
        self.bank.deposit("1", 100_000)
        self.assertEqual(100_000, self.bank.check_balance("1", "1234"))
        self.bank.transfer("1", "2", 20_000, "1234")
        self.assertEqual(80_000, self.bank.check_balance("1", '1234'))

