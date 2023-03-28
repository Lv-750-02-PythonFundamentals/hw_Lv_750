class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def species(cls):
        return "This individual belongs to the species Homo sapiens."

    @staticmethod
    def arbitrary_message():
        return "Hello Alien."


person = Human("Andrii")


person.welcome()


print(Human.species())


print(Human.arbitrary_message())
