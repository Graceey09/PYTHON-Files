from class_work.custom_exception_class import AccountErrorException
from java_task_in_python.account import Account


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.account_collection = []

    def generate_account_number(self):
        # account_number = random.randint(1000000000, 9999999999)
        return str(len(self.account_collection) + 1)

    def register(self, first_name, last_name, pin):
        account_name = f'{first_name} {last_name}'
        account = Account(self.generate_account_number(), account_name, pin)
        self.account_collection.append(account)

    def find_account(self, account_number):
        for account in self.account_collection:
            if account.get_account_number() == account_number:
                return account
        raise AccountErrorException('Account not found oo')

    def withdraw(self, account_number , amount, pin):
        self.find_account(account_number).withdraw(amount, pin)

    def check_balance(self, account_number, pin):
        return self.find_account(account_number).check_balance(pin)

    def deposit(self, account_number, amount):
        self.find_account(account_number).deposit(amount)

    def transfer(self, senders_account, receiver_account, amount, pin):
        sender = self.find_account(senders_account)
        sender.withdraw(amount, pin)

        receiver = self.find_account(receiver_account)
        receiver.deposit(amount)



