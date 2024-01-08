class ProgrammerRoles:
    def __init__(self, lang, projects=None):
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def get_info(self):
        return f"Name: {self.faritName} {self.lastName} \njob: {self.__class__.__name__}"

    def assign_project(self, project):
        self.projects.append(project)

    def get_ptojects(self):
        print("projects:")
        print("-"*20)
        projects_list = []
        for num, project in enumerate(self.projects):
            projects_list.append(f"{num + 1}. {project}")
        return '\n'.join(projects_list)

class ManagerRoles:
    def __init__(self, employees=None):
        if employees is None:
            employees = []
        self.employees = employees

    def get_employees(self):
        print ("Employees:") 
        print ("="*20)
        employees_list = []
        for num, employee in enumerate(self.employees):
            employees_list.append(f"{num + 1}. {employee.get_info()}")
        return '\n'.join(employees_list)

    def get_info(self):
        return f"Name: {self.faritName} {self.lastName} \njob: {self.__class__.__name__}"