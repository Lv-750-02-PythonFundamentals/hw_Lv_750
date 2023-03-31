"""Homework 10 task 3"""


class Employee:
    """Class employee"""
    EMPLOYEE_COUNT = 0
    employee_list = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EMPLOYEE_COUNT += 1
        Employee.employee_list.append(f"id:{self.EMPLOYEE_COUNT}. name: {self.name}, salary: {self.salary}")

    def employee_info(self):
        return f"Name : {self.name}, salary : {self.salary}"

    @classmethod
    def e_list(cls):
        return cls.employee_list

    @classmethod
    def employee_count(cls):
        return cls.EMPLOYEE_COUNT


employee_1 = Employee("James", 1200)
employee_2 = Employee("Valera", 1300)

print(employee_1.employee_info())
print(employee_2.employee_info())
print(employee_2.employee_count())
print(Employee.e_list())
print(Employee.employee_list[0])

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
