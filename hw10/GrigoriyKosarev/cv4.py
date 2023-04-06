class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = self.getInfo()


    def getInfo(self):
        return f"{self.name}s age is {self.age}"


print(Person("john", 16).getInfo())



