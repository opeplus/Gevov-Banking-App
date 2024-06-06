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
