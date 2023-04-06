
class Employee():
    """Emploee description"""

    total_employees = 0

    def __init__(self, name, salary):
        Employee.total_employees += 1
        self.name = name
        self.salary = salary

    def info(self):
        print(f"name: {self.name}\nsalary: {self.salary}")
    @staticmethod
    def print_total_employees():
        print(Employee.total_employees)

employee1 = Employee("Bob", 1000)
employee2 = Employee("Tom", 1500)

employee1.info()
employee2.info()
Employee.print_total_employees()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)