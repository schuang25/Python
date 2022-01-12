class Pet:
    def __init__(self, name, type="", tricks=[]):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 30

    def sleep(self): # increases the pets energy by 25
        self.energy += 25
        return self
    
    def eat(self): # increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        return self
    
    def play(self): # increases the pet's health by 5
        self.energy -= 10
        self.health += 5
        return self
    
    def noise(self): # prints out the pet's sound
        print(self.name + " makes a noise.")
        return self
