from pet import Pet
from dog import Dog

class Ninja:
    def __init__(self, first_name, last_name, treats=3, pet_food=2, pet=Pet("Fido")):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    
    def walk(self): # walks the ninja's pet invoking the pet play() method
        print("Walking " + self.pet.name)
        self.pet.play()
        return self

    def feed(self): # feeds the ninja's pet invoking the pet eat() method
        if (self.pet_food > 0):
            print("Feeding " + self.pet.name)
            self.pet.eat()
            self.pet_food -= 1
        else:
            print("Not enough pet food to feed " + self.pet.name + "!")
        return self

    def bathe(self): # cleans the ninja's pet invoking the pet noise() method
        print("Giving " + self.pet.name + " a bath")
        self.pet.noise()
        return self

ninja = Ninja("Bob", "C", 3, 2, Dog("Fido"))
ninja.walk()
ninja.feed()
ninja.bathe()