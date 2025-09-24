class bankaccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        print (f"Account Number: {self.account_number} Deposited amount: {self.deposit_amount}, Balance: {self.balance}")

    def withdraw (self, withdrawn_amount):
        self.withdrawn_amount = withdrawn_amount
        self.balance -= withdrawn_amount
        print(f"You have withdrawn {self.withdrawn_amount}, Balance: {self.balance}")

acc11 = bankaccount(1122334455,0)
acc11.deposit(5000)
acc11.deposit(5500)
acc12 = bankaccount(1213141516,500)
acc12.deposit(45000)
acc12.withdraw(3300)

                


        