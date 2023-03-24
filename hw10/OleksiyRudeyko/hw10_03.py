class Employee:
    employee_num = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_num += 1

    @classmethod
    def total_number_of_employees(cls):
        print(f"Total number of employees: {cls.employee_num}")

    def employee_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

print(Employee.__base__) 
print(Employee.__dict__) 
print(Employee.__name__) 
print(Employee.__module__) 
print(Employee.__doc__)
