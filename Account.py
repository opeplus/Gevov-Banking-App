class Account:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance
        self._interest_rate = 0

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def get_interest_rate(self):
        return self._interest_rate

    def deposit(self, amount):
        self._balance += amount
        self._apply_interest()
        print(f"New balance is: {self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is: {self._balance}")
        else:
            print("Insufficient funds.")

    def _apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
