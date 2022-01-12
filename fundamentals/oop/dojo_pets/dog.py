from pet import Pet

class Dog(Pet):
    def __init__(self, name, type="dog", tricks=[]):
        super().__init__(name, type)
    
    def noise(self): 
        print(self.name + " barks.")
        return self