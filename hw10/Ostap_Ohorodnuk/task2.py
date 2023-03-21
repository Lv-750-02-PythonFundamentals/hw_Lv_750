"""Homework 10 task 2"""

class Human:
    """class Human"""
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome {self.name}"

    @classmethod
    def species(cls):
        pass
        return " Homosapiens "

    @staticmethod
    def some_message():
        return "Welcome to Lviv"


human = Human("Pavlo")
print(human.welcome_message(), human.species(), human.some_message())
