class Walletsystem:
    def __init__(self,balance=0):
        self.totalBalance=balance
    
    def add_funds(self,amount):
        if amount>=0:
            self.totalBalance+=amount
            return True
        else:
            return False
    
    def make_payment(self,amnt):
        if self.totalBalance>amnt:
            self.totalBalance-=amnt
            return True
        else:
            print("Insufficient fund oops!")
            return False
    
    def get_balance(self):
        return self.totalBalance
    
    def transfer(self,amnt,recipient):
        if amnt<self.get_balance():
            self.totalBalance-=amnt
            recipient.add_funds(amnt)
            return True
        else:
            return False