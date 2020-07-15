class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance:${self.balance}"
    def deposite(self,amount):
        self.balance += amount
        print("Deposite accepted!")
    def withdraw(self,amount):
        if self.balance<amount:
            print("Amount unavailable!!!")
        else:
            self.balance -= amount
            print("Withdraw accepted!")

acct1 = Account('Jose',100)
print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposite(50)

acct1.withdraw(75)

acct1.withdraw(500)