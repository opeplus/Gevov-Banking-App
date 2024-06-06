current_account.py:from Account import Account

class CurrentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

current_account = CurrentAccount("CA001", 10000)
current_account.deposit(2000)
print(f"Current balance: {current_account.balance}")
