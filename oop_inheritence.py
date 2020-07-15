class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def speak(self, sound):
        return f"{self.name} barks: {sound}."
    
class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachsund(Dog):
    pass

class BullDog(Dog):
    pass


miles = JackRusselTerrier("Miles", 4)
buddy = Dachsund("buddy",9)
jack = BullDog("jack",3)
jim = BullDog("jim",5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("woof"))

print(type(miles))
print(isinstance(miles,Dog))
print(isinstance(miles,BullDog))

print(miles.speak())
#print(miles.speak("Grrrr"))