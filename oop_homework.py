#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line(object):
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return ((y2-y1)/(x2-x1))
    
a = Line((3,2),(8,10))

print(a.distance())
print(a.slope())
         


#problem 2
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return 3.14 * self.radius**2 * self.height
    
    def surface_area(self):
        return 2*3.14*self.radius*(self.radius+self.height)

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())
