from Account import Account

class StudentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self._withdrawal_limit = 2000
        self._deposit_limit = 50000

    def deposit(self, amount):
        if amount <= self._deposit_limit:
            super().deposit(amount)
        else:
            print("Deposit limit exceeded")

    def withdraw(self, amount):
        if amount <= self._withdrawal_limit:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded")

student_account = StudentAccount("StA001", 10000)
student_account.deposit(60000)
student_account.withdraw(6000)
print(f"Current balance: {student_account.balance}")
