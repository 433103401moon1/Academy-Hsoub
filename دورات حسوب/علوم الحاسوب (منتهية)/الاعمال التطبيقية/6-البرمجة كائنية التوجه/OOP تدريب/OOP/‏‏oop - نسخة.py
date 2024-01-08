import datetime
from abc import ABC, abstractmethod

class Employee(ABC):
    # 05. خصائص وتوابع الأصناف Class Properties and Methods
    totall = 0
    salary_raise = 1.5

    def __init__(self, faritName, lastName, salary):
        self.faritName = faritName
        self.lastName = lastName
        # self.title = title
        Employee.totall += 1
        # 08. التغليف Encapsulation
        self.__salary = salary
    
    def get_info(self):
        return f"Name: {self.faritName} {self.lastName} \nsalary: {self.salary}"
    
    # 08. التغليف Encapsulation --1
    # def get_salary(self):
    #     return self.__salary
    # def set_salary(self, salary):
    #     if salary <= 0 :
    #         raise ValueError
    #     self.__salary = salary
    
    # 08. التغليف Encapsulation --2
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        if salary <= 0 :
            raise ValueError
        self.__salary = salary
    

    # 05. خصائص وتوابع الأصناف Class Properties and Methods 
    @classmethod
    def change_raise(cls, amount):
        cls.salary_raise = amount
        
    # 05. خصائص وتوابع الأصناف Class Properties and Methods
    @classmethod
    def from_string(cls, string):
        faritName, lastName, salary = string.split('-')
        salary = int(salary)
        return cls(faritName, lastName, salary)

    #	06. التوابع الساكنة Static Methods 
    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True
    

class Manager(Employee):
    def __init__(self, firstName, lastName, salary, employees ):
        super().__init__(firstName, lastName, salary)
        self.employees = employees

    def get_employees(self):
        print ("Employees:")
        print ("="*20)
        employees_list = []
        for num, employee in enumerate(self.employees):
            employees_list.append(f"{num + 1}. {employee.get_info()}")
        return '\n'.join(employees_list)

class Accountant:
    pass

class Programmer(Employee):
    def __init__(self,firstName, lastName, salary, lang, projects):
        super().__init__(firstName, lastName, salary)
        self.lang = lang
        self.projects = projects

    def get_ptojects(self):
        print("projects:")
        print("-"*20)
        projects_list = []
        for num, project in enumerate(self.projects):
            projects_list.append(f"{num + 1}. {project.get_info()}")
        return '\n'.join(projects_list)

class project:
    def __init__(self, name, description, days, done):
        self.name = name
        self.description = description
        self.days = days
        self.done = done
    def get_info(self):
        return f"name: {self.name}, description: {self.description}, days: {self.days}, done: {self.done}"

# ----------------------------------------------------------------

# ahmed = Employee.from_string("ahmed-ali-mahager-8500")
# print(ahmed.get_info())
# print(ahmed.salary)

# date = datetime.date(2023,11,15)
# print(Employee.is_workday(date))

# print(ahmed.get_salary())
# ahmed.set_salary(2000)
# print(ahmed.get_salary())
# ahmed.set_salary(0)

# ali = Employee.from_string("ali-ali-1111")
# # mohamed = Manager.from_string("mohamed-ali-2222")
# ahmed = Manager("ahmed", "ali", 3333, [ali])

# print(ahmed.get_employees())

project1 = project("project1", "description1", 20, True)
project2 = project("project2", "description2", 10, False)
project3 = project("project3", "description3", 1, True)
project4 = project("project4", "description4", 4, False)

programmer_ahmed = Programmer("ahmed", "ali", 5500, ["python", "java", " c++"], [project1, project3, project4])
# print(programmer_ahmed.projects[0].name)
print(programmer_ahmed.get_ptojects())
