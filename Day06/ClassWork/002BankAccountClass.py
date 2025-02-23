class BankAccount:
    def __init__(self,holder_name,account_number,balance=0):
        self.account_holder=holder_name #attribute can any name 
        self.account_number=account_number
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print(f"Deposited {amount} ,new Balance: {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Fund")
        else:
            self.balance-=amount
            print(f"Withdrawn {amount} ,Remaining Balance : {self.balance}")
account1=BankAccount("prashant kumar","1223323",600)
print(f"Account Holder: {account1.account_holder}")
print(f"Balance: {account1.balance}")
account1.deposite(200)
account1.withdraw(100)
account1.withdraw(1000)