class Account:
    def __init__(self, account_number, account_name, pin):
        self.__balance = 0.0
        self.account_name = account_name
        self.account_number = account_number
        self.pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("invalid input")

    def check_balance(self, pin):
        self.__validate_pin(pin)
        return self.__balance

    def withdraw(self, amount, pin):
        self.validate_withdrawal(amount)
        self.__validate_pin(pin)
        self.__balance -= amount

    def __validate_pin(self, pin):
        if self.pin != pin:
            raise ValueError("Wrong Pin")

    def validate_withdrawal(self, amount, error=ValueError("Insufficient Balance")):
        if amount < 0:
            raise ValueError("Invalid Input")
        if amount > self.__balance:
            raise error

    def update_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            return new_pin

    def get_name(self):
        return self.account_name

    def get_account_number(self):
        return self.account_number
