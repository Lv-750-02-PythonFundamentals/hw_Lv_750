
class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)
    
    def make_sound(self):
        return "Roar"
    
    def give_birth(self):
        pass


class Bird(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)
    
    def make_sound(self):
        return "Squawk"
    
    def lay_eggs(self):
        pass


class Reptile(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)
    
    def make_sound(self):
        return "Hiss"
    
    def shed_skin(self):
        pass


animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]

for animal in animals:
    print(f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}")