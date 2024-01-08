from Employee import Employee

class Accountant(Employee):
    def __init__(self, firstName, lastName, salary, groups):
        super().__init__(firstName, lastName)
        self.salary = salary
        self.groups = groups
    
    def get_info(self):
        return f"Name: {self.faritName} {self.lastName} \nsalary: {self.salary} \ngroups: {self.groups}"
    
    def calculate_salary(self):
        pass
    
    @classmethod
    def from_string(cls, string):
        faritName, lastName, salary = string.split('-')
        salary = int(salary)
        return cls(faritName, lastName, salary)
        
    def assign_groups(self, group):
        self.groups.append(group)
