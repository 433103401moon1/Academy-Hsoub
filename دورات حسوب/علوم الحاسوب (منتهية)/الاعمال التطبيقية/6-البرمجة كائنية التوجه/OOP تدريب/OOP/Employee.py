import datetime
from abc import ABC, abstractmethod

class Employee(ABC):
    
    totall = 0

    def __init__(self, fristName, lastName):
        self.fristName = fristName
        self.lastName = lastName
        self.profile = None
        Employee.totall += 1
    
    @abstractmethod
    def get_info(self):
        return f"Name: {self.fristName} {self.lastName}"
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    @classmethod
    # @abstractmethod
    def from_string(cls, string):
        fristName, lastName = string.split('-')
        return cls(fristName, lastName)

# class Freelancer(Employee):
#     def __init__(self, fristName, lastName, hour_rate, work_hours):
#         Employee.__init__(self, fristName, lastName)
#         self.hour_rate = hour_rate
#         self.work_hours = work_hours
    
#     def get_info(self):
#         return f"Name: {self.fristName} {self.lastName} \njob: {self.__class__.__name__}"
    
#     def calculate_salary(self):
#         return self.hour_rate * self.work_hours
    
#     @classmethod
#     def from_string(cls, string):
#         fristName, lastName, hour_rate, work_hours = string.split('-')
#         hour_rate, work_hours = int(hour_rate), int(work_hours)
#         return cls(fristName, lastName, hour_rate, work_hours)
