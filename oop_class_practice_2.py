class Customer:
    
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return f"Customer name is {self.name} and balance is {self.balance}"
    
    def withdraw(self, amount):
        if amount> self.balance:
            raise RuntimeError("amount is greater than balance")
        self.balance -= amount
        return self.balance
    
    def deposite(self, amount):
        self.balance += amount
        return self.balance
    @staticmethod
    def message():
        return "Customer is our first priority!!!"
    
    

naim = Customer("Naim Hasan", 10000)
print(naim)

naim.deposite(5000)
print(naim)

naim.deposite(5000)
print(naim)

naim.withdraw(7000)
print(naim)

print(naim.message())
        