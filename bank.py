class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        print(self.name, self.balance, self.min_balance)
    def deposit(self, amount):
        self.balance += amount
        
        return "updated balance is: {}".format(self.balance)
        
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            return "debited amount is:{} and updated balance is:{}".format(amount, self.balance)
            
        else:
            print("Sorry, not enought funds.")
    def statement(self):
        print("Account Balance: PLN{}".format(self.balance))
        

obj1=Account('ckm', 15000, 100)
obj2=Account('mkm', 20000, 100)
obj3=Account('snk', 25000, 100)
obj4=Account('ubr', 35000, 100)
l=[obj1.name, obj2.name, obj3.name, obj4.name]
print("WELCOME TO BANK")
print("SELECT THE SERVICE ")
print("1. Deposit\n 3. Withdraw\n")
name=input("enter your name:\n")
if(name in l):
    choice=int(input("enter your choice"))
    if(choice==1):
        print("the selected service is Deposit\n")
        amount=int(input("enter the amount to be deposited\n"))
        if(name==obj1.name):
            res=obj1.deposit(amount)
            print(res)
        elif(name==obj2.name):
            res=obj2.deposit(amount)
            print(res)
        elif(name==obj3.name):
            res=obj3.deposit(amount)
            print(res)
        elif(name==obj4.name):
            res=obj4.deposit(amount)
            res=obj4.statement()
            
    else:
        print("the selected service is withdraw\n")
        amount=int(input("enter the amount to be deposited\n"))
        if(name==obj1.name):
            res=obj1.withdraw(amount)
            print(res)
        elif(name==obj2.name):
            res=obj2.withdraw(amount)
            print(res)
        elif(name==obj3.name):
            res=obj3.withdraw(amount)
            print(res)
        elif(name==obj4.name):
            res=obj4.withdraw(amount)
            print(res)
else:
    print("Unauthorized Access\n")
            

           

