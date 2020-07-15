import math

class Circle:
    pi = math.pi
    
    def __init__(self,radius=1):
        self.radius = radius
        self.area = Circle.pi * radius**2
    
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius*new_radius*Circle.pi
        
    def getCircumfurence(self):
        return self.radius*Circle.pi*2
    
    def __str__(self):
        return f"Circle radius is {self.radius}, area is {self.area}"
    def __del__(self):
        print("Object is destroyed")

c = Circle()
print(c)
print(c.area)
print(c.getCircumfurence())

c.setRadius(4)

print(c)
print(c.area)
print(c.getCircumfurence())
del c

    
    
    