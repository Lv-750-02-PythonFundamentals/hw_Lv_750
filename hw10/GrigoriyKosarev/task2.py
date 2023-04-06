
class Human():
    """Human description"""

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello! {self.name}")

    def info(self):
        print(f"Human is a Homosapiens")

    @staticmethod
    def class_info():
        print("This is Human class")


human = Human("Bob")
human.say_hello()
human.info()

Human.class_info()


