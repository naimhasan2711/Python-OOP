class Dog:
    
    #class instance
    species = "Same for all"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    #another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
A = Dog("jacky",5)

print(A)
print(A.speak("woof woof"))



        
    