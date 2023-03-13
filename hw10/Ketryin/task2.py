# Task2. Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:
    SPECIES = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcom_message(self):
        return f"Hello, {self.name}"

    @classmethod
    def species(cls):
        return cls.SPECIES
    
    @staticmethod
    def message():
        return "Hello"

human = Human("Petro")
print(human.welcom_message())
print(Human.species())
print(Human.message())