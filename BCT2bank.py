from datetime import datetime #BCT2
class Bank_Account:
 def __init__(self):
 self.balance=0
 self.timestamp=datetime.now()
 def deposit(self):
 amount=float(input("Enter amount to be Deposited: "))
 self.timestamp=datetime.now()
 self.balance += amount
 print("\n Amount Deposited:",self.balance)
 def withdraw(self):
 amount = float(input("Enter amount to be Withdrawn: "))
 if self.balance>=amount:
 self.timestamp=datetime.now()
 self.balance-=amount
 print("\n You Withdrew:", amount)
 else:
 print("\n Insufficient balance ")
 def display(self):
 print("\n Net Available Balance=",self.balance)
 print("\n Timestamp=",self.timestamp)
print("Enter the choice:")
print("1. Deposit")
print("2. Withdraw")
print("3. Display")
print("0. Exit")
accounts_detail = {
 '15':{'name':'a','acc': '15','balance':0,
 'secret_key':'1asd23asdf456789a',
 'obj':Bank_Account()
 },
 '25':{'name':'b','acc': '25','balance':0,
 'secret_key':'1asd23asdf456789b',
 'obj':Bank_Account()
 },
 '35':{'name':'c','acc': '35','balance':0,
 'secret_key':'1asd23asdf456789c',
 'obj':Bank_Account()
 },
 '45':{'name':'d','acc': '45','balance':0,
 'secret_key':'1asd23asdf456789d',
 'obj':Bank_Account()
 },
 '55':{'name':'e','acc': '55','balance':0,
 'secret_key':'1asd23asdf456789e',
 'obj':Bank_Account()
 },
 '65':{'name':'f','acc': '65','balance':0,
 'secret_key':'1asd23asdf456789f',
 'obj':Bank_Account()
 }
}
while True:
 choice=int(input("Enter the choice: "))
 acc=(input("Enter acc no.: "))
 secret_key = input("Enter a secret id: ") 
 if secret_key != accounts_detail[acc]['secret_key']:
 print("Authentication fail..secret key does not match...with your id")
 continue
 if(choice==1):
 accounts_detail[acc]['obj'].deposit()
 elif(choice==2):
 accounts_detail[acc]['obj'].withdraw()
 elif(choice==3):
 accounts_detail[acc]['obj'].display()
 elif choice == 0:
 break
 else:
 print("Enter proper input!!!")
