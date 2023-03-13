# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)

class Employee:
    EMPLOYEES_COUNT = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EMPLOYEES_COUNT += 1
        
    def print_employees_info(self):
        print(f"Name - {self.name}, salary - {self.salary}")

    @classmethod
    def print_employees_count(cls):
        print(cls.EMPLOYEES_COUNT)

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation bar:", Employee.__doc__)

    

    