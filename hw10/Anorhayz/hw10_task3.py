class Employee:
    """
    Class with information about every employee
    """
    EMPLOYEE_COUNT = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EMPLOYEE_COUNT += 1

    def employee_info(self):
        return f"Employee name: {self.name}, employee salary: {self.salary}"

    @classmethod
    def employee_count(cls):
        return cls.EMPLOYEE_COUNT


employee_num1 = Employee("James", 1200)
print(employee_num1.employee_info())
print(employee_num1.employee_count())


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
