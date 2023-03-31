class Polygon:
    pass


class Rectangle(Polygon):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_square(self):
        return f"The square of rectangle is {self.x * self.y}"


class Human:
    SPECIES = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}"

    @classmethod
    def display_species(cls):
        return cls.SPECIES

    @staticmethod
    def say_bye():
        return "Bye, bye"


class Employee:
    """Employees of company"""
    num_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1

    def display_employee(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def display_total_employees(cls):
        return f"Total Employees: {cls.num_employees}"


if __name__ == "__main__":
    rectangle = Rectangle(12, 20)
    man = Human("John")
    employee_1 = Employee("Frank", 5000)
    employee_2 = Employee("Chris", 5000)
    print(rectangle.calc_square())
    print(man.say_hello())
    print(man.SPECIES, man.say_bye())
    print(employee_1.display_employee())
    print(Employee.display_total_employees())
    print("Base class:", Employee.__base__)
    print("Class namespace:", Employee.__dict__)
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Documentation bar:", Employee.__doc__)
