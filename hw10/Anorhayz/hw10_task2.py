class Human:
    SPECIES = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_msg(self):
        return f"Welcome, {self.name}"

    @classmethod
    def human_species(cls):
        return cls.SPECIES

    @staticmethod
    def free_message():
        return "Have a nice day"


random_human = Human("Gustavo")
print(random_human.welcome_msg())
print(random_human.human_species())
print(random_human.free_message())
