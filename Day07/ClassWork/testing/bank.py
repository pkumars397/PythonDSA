class Bankaccount:
    def __init__(self,initial_balance=0):
        self.total_balance=initial_balance
    def deposite(self,amount):
        if amount<0:
            print("You can't deposite less than 0")
            return False
        else:
            self.total_balance+=amount 
            return True
    def withdraw(self,amnt):
        if self.total_balance>amnt and amnt>0:
            self.total_balance-=amnt 
            return True
        else:
            print("Insufficient balance")
            return False 
    def get_balance(self):
        return self.total_balance