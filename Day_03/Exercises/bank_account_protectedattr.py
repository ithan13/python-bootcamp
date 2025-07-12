class Bank_Account:
    def __init__(self, initial_balance=999):
        self._balance = initial_balance

    def deposit(self,deposit):
        self._balance += deposit

    def withdraw(self, withdraw):
        self._balance -= withdraw

    def print_balance(self, print_balance):
        print(self._balance)

bank_total = Bank_Account()
# bank_total.withdraw(500)
bank_total.deposit(800)

print("Bank Account Balance",bank_total._balance)





