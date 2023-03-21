class Human:
    species = "Homosapiens"
    
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def get_species(cls):
        return cls.species
    
    @staticmethod
    def get_arbitrary_message():
        return "Arbitrary message."
