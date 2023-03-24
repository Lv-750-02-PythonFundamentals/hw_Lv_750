"""Create a class Human, everyone has a name, create a method in the
class that displays a welcome message to each person. Create a class method
in the class that returns information that it is a species of "Homosapiens". And
in the class create a static method that returns an arbitrary message.
"""

class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello {self.name}")

    @classmethod
    def info(cls):
        return "species of 'Homosapiens'"
    
    @staticmethod
    def msg():
        return "arbitrary message"

victor = Human("Victor")
victor.welcome()

print(Human.info())
print(victor.info())

print(Human.msg())
print(victor.msg())