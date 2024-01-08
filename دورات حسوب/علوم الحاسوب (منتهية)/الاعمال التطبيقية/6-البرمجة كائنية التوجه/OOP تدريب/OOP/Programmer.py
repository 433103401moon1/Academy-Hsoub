from Employee import Employee #, Freelancer
from Payments import *
from Roles import *

class Programmer(Employee, ProgrammerRoles, Salary):
    def __init__(self,firstName, lastName, salary, lang, projects=None):
        Employee.__init__(self, firstName, lastName)
        ProgrammerRoles.__init__(self, lang, projects)
        Salary.__init__(self, salary)
        # self.salary = salary
        # self.lang = lang
        # if projects is None:
        #     projects = []
        # self.projects = projects

    def get_info(self):
        return f"Name: {self.faritName} {self.lastName} \njob: {self.__class__.__name__}"
    
    def calculate_salary(self):
        return Salary.calculate_salary(self)
    
    @classmethod
    def from_string(cls, string):
        faritName, lastName, salary, lang = string.split('-')
        salary = int(salary)
        return cls(faritName, lastName, salary, lang)


    def get_ptojects(self):
        print("projects:")
        print("-"*20)
        projects_list = []
        for num, project in enumerate(self.projects):
            projects_list.append(f"{num + 1}. {project.get_info()}")
        return '\n'.join(projects_list)

class FreelancerProgrammer(Employee, ProgrammerRoles, HourlyPayment):
    def __init__(self, fristName, lastName, lang, projects, hour_rate, work_hours):
        Employee.__init__(self, fristName, lastName)
        ProgrammerRoles.__init__(self, lang, projects)
        HourlyPayment.__init__(self, hour_rate, work_hours)
    
    def get_info(self):
        return f"Name: {self.faritName} {self.lastName} job: {self.__class__.__name__} \nhour rate: {self.hour_rate}"
        
    def calculate_salary(self):
        return HourlyPayment.calculate_salary(self)
