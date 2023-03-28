class Employee:
    """Сounting the number of employees"""
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def __str__(self):
        return f"Employee: {self.name}, salary: {self.salary}"

    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")


employee1 = Employee("John", 50000)
employee2 = Employee("Mary", 55000)


print(employee1)
print(employee2)


Employee.print_total_employees()


print("Basic classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)