class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage
        
    def __str__(self):
        return f"the {self.color} car has {self.milage} miles"
blue_car = Car("blue",20000)
red_car = Car("red",30000)

for car in (blue_car,red_car):
    print(f"The {car.color} has {car.milage:,} miles")


