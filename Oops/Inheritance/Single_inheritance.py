class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makeSound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def makeSound(self):
        print("Bark")

d = Dog("Dog", "Bark")
d.makeSound()

d = Animal("Dog", "Bark")
d.makeSound()

