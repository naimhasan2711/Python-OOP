class Bangladesh:
    
    def capital(self):
        print("Dhaka is tha capital of Bangladesh")
        
    def language(self):
        print("Bangla is the native language of Bangladesh")
        
    def type(self):
        print("Bangladesh is a developing country")

class USA:
    
    def capital(self):
        print("Washington DC is the capital of USA")
    
    def language(self):
        print("English is the native language of USA")
    
    def type(self):
        print("USA is a developed country")
    
b = Bangladesh()
u = USA()

for country in(b,u):
    country.capital()
    country.language()
    country.type()