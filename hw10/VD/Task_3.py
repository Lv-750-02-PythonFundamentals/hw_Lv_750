"""Create an employee class. Each employee has characteristics such as name
and salary. The class should have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
name and salary.
In addition to creating a class, display information about the base classes from which
the employee class is inherited (__base__), the class namespace (__dict__), the
class name (__name__), the module name in which the class is defined
(__module__), the documentation bar ( __doc__)
"""

class Employee:
    """Task_3"""
    counter = 0
    total = {}
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
        Employee.total.update({self.name : self.salary})

    def numb_of_employees():
        print(Employee.counter)
    
    def info(self):
        print(f"name {self.name}, salary {self.salary}")

    def total_info():
        for i in Employee.total:
            print(f"name {i}, salary {Employee.total[i]}")
        
    
    
        

vd = Employee("VD", 100)
sv = Employee("SV", 120)
hw = Employee("HW", 50)
sw = Employee("Andrii", 75)
print("-------------------------")
Employee.numb_of_employees()
print("-------------------------")
vd.info()
hw.info()
Employee.info(vd)
print("-------------------------")
Employee.total_info()
print("-------------------------")
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)