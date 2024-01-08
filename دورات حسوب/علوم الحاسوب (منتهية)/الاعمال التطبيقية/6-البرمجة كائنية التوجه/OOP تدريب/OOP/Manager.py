from Employee import Employee
from Payments import *
from Roles import *

class Manager(Employee, Salary, ManagerRoles):
    def __init__(self, firstName, lastName, salary, employees=None ):
        Employee.__init__(self, firstName, lastName)
        Salary.__init__(self, salary)
        ManagerRoles.__init__(self, employees)
        # self.salary = salary
        # self.employees = employees

    def get_employees(self):
        print ("Employees:")
        print ("="*20)
        employees_list = []
        for num, employee in enumerate(self.employees):
            employees_list.append(f"{num + 1}. {employee.get_info()}")
        return '\n'.join(employees_list)

    def get_info(self):
        return f"Name: {self.fristName} {self.lastName} \nsalary: {self.salary}"
    
    def calculate_salary(self):
        pass
    
    @classmethod
    def from_string(cls, string):
        faritName, lastName, salary = string.split('-')
        salary = int(salary)
        return cls(faritName, lastName, salary)
    
class FreelancerManager(Employee, ManagerRoles, HourlyPayment):
    def __init__(self, firstName, lastName , employees, hour_rate, work_hours):
        Employee.__init__(self, firstName, lastName)
        ManagerRoles.__init__(self, employees)
        HourlyPayment.__init__(self, hour_rate, work_hours)

    def get_info(self):
        return f"Name: {self.faritName} {self.lastName} job: {self.__class__.__name__} \nhour rate: {self.hour_rate}"
    
    def calculate_salary(self):
        return HourlyPayment.calculate_salary(self)