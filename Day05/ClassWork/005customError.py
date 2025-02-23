def withdraw(balance,amnt):
 if balance >=amnt:
  return balance-amnt
 else:
  raise ValueError("Insufficient funds")

try:
 bal=int(input("Enter your balance: "))
 withdrawAmnt=int(input("Enter you withdrawal amount"))
 newBal=withdraw(bal,withdrawAmnt)
 print("Transaction Successful! remaining Balance: ",newBal)
except ValueError as e:
 print("Transaction Declined ",e)
 
