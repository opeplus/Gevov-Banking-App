from Account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self._interest_rate = 0.005
        self._withdrawal_limit = 700000

    def withdraw(self, amount):
        if amount <= self._withdrawal_limit:
            super().withdraw(amount)
        else:
            print("You cannot withdraw above your limit")

savings = SavingsAccount("SA001", 10000)
savings.deposit(3000)
savings.withdraw(2000)
savings.withdraw(1500)
print(f"Current balance: {savings.balance}")
children_account.py:from Account import Account
children_account.py:from Account import Account

class ChildrenAccount(Account):
    def _init_(self, account_number, balance=0):
        super()._init_(account_number, balance)
        self._interest_rate = 0.007

    def withdraw(self, amount):
        print("Withdrawals are not allowed for a Children's account")

children_account = ChildrenAccount("ChA001", 10000)
children_account.deposit(2000)
print(f"Current balance: {children_account.balance}")
