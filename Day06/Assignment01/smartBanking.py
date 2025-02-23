class BankAccount:
    #Represent a basic bank account for customers
    #bank_name as class variables shared to all instances of class
    bank_name="SmartBank"
    def __init__(self,account_number,account_holder,balance):
        self.acc_number=account_number
        self.account_holder=account_holder
        self.Total_balance=balance
    def __str__(self):
        #returns account details as a string
        return (f"Your account Details: \nAccount Number: {self.acc_number}\nAccount Holder: {self.account_holder} \nAvailable Balance={self.Total_balance}")
    
    def deposite(self,amount):
        if amount>0:
          self.Total_balance+=amount 
          print(f"${amount} deposited successfully.New Balance: ${self.Total_balance}")
        else:
          print("Deposite amount must be positive.")

    def withdraw(self,amount):
        if amount>self.Total_balance:
            print(f"Insufficient Fund!")
        elif amount<=0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.Total_balance-=amount 
            print(f"You withdrawn ${amount}.  Remaining Balance: ${self.Total_balance}")
    def get_balance(self):
        return self.Total_balance
    
    @staticmethod
    def bank_policy():
        #this method will do nothing it has same task for every instances(objecrs of class),so it doesn't need the data of objects created
        print("SmartBank Policy:Minimum balance $100,Withdrawal limit for normal accounts: $5000")

#Premium Account Class
class PremiumAccount(BankAccount):
    def __init__(self,account_number,account_holder,balance):
        super().__init__(account_number,account_holder,balance)
        self.rewardPoints=0

    def earn_rewards(self,amount):
       #earn 1 rewards point for each $100 deposite
       self.rewardPoints+=(amount//100)
       print(f"Reward earned: {amount//100} points && Total Rewards Points: {self.rewardPoints} Points")

    def withdraw(self, amount):
        #allow user higher withdrawal limit for premium customers
        if self.Total_balance<amount:
            print("Insufficient balance")
        elif amount<=0:
            print("Withdrawal amount must be greater than zero.")
        else:
            if amount<=10000:
                self.Total_balance-=amount 
                print(f"withdrawn ${amount}.Remaining Balance : ${self.Total_balance}.")
            else: 
                print("Withdraw limit exceeded! Please enter a lower amount")
    def __str__(self):
        return super().__str__()+f"\nrewards points: {self.rewardPoints}"

#BankManager class
class BankManager:
    def __init__(self):
        self.listOfAcc=[]

    def add_account(self,acc):
        self.listOfAcc.append(acc)
        print(f"Account {acc.acc_number} added successfully.")

    def view_all_accounts(self):
        print("-----All accounts details----")
        for account in self.listOfAcc:
            print(account)
        print("-"*30)

    def close_account(self,acc):
        if acc in self.listOfAcc:
           self.listOfAcc.remove(acc)
           print(f"Account {acc.acc_number} has been closed")
        else:
           print(f"Account not found") 
    
    def get_role(self):
        #role of the manager
        return "Bank Manager"

#Implementing system now

if __name__=="__main__":
    print("\n🚀 Welcome to SmartBank Banking System 🏦\n")
    
    #creating accounts
    prashant_acc=BankAccount("12345","Prashant Kumar",10000)
    binu_acc=PremiumAccount("67889","Binu Kumar",5000)
    
    #Displaying Account details
    print(prashant_acc)
    print(binu_acc)
    
    #transactions
    print("\n Depositing Money: ")
    prashant_acc.deposite(5000)
    binu_acc.deposite(15000)

    print("\nWithdrawing Money: ")
    prashant_acc.withdraw(2000)
    binu_acc.withdraw(10000)

    #earn points for premium account
    binu_acc.earn_rewards(5000)
    binu_acc.earn_rewards(5000)

    #Bank manager
    manager=BankManager()
    print("\n Adding Accounts to the Bank System: ")
    manager.add_account(prashant_acc)
    manager.add_account(binu_acc)
    print("\n Viewing All customer Accounts: ")
    manager.view_all_accounts()
    print("\n Closing an Account: ")
    manager.close_account(prashant_acc)
    print("\nUpdated database of accounts")
    manager.view_all_accounts()

    print("\nSmartBank system implemented successfully!")