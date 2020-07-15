
 class Vehicle(object):
    
    base_sale_price = 0.0
    
    
    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        
    def sale_price(self):
        if self.sale_price is not None:
            return 0.0
        return 5000.0 * self.wheels
    
    def purchase_price(self):
        if self.sold_on is None:
            return 0.0
        return self.base_sale_price - (.10 * self.miles)
    
class Car(Vehicle):
    
    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        
        
class Truck(Vehicle):
    
    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        
v = Vehicle(4, 0, 'Honda', 'Accord', 2014, None)

print(v.purchase_price())


    
