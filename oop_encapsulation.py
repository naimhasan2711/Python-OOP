# below code is for demostrate protected members

class Base:
    def __init__(self):
        self._a = 2
        
        
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of Base class: ")
        print(self._a)
obj1 = Derived()
obj2 = Base()
print(obj2.a) 
    
    
#below code is for demonstrate private members
class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling private member of base class: ") 
        print(self.__a) 
# Driver code 
obj1 = Base() 
print(obj1.a) 