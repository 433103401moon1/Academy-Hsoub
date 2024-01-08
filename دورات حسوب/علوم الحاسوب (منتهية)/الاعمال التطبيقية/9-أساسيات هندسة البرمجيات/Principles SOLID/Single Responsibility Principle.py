# Bad example
class Employee:
    def __init__(self, name, jop, user_name, password, is_locked, company_name, company_address):
        self.name = name
        self.jop = jop
        self.user_name = user_name
        self.password = password
        self.is_locked = is_locked
        self.company_name = company_name
        self.company_address = company_address   
# e = Employee("alice", "jop", "user_name", "password", "is_locked", "company_name", "company_address")
# print(e.company_address)


# Good example
class Employee:
    def __init__(self, name, jop):
        self.name = name
        self.jop = jop

class Company:
    def __init__(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address

class User:
    def __init__(self, user_name, password, is_locked):
        self.user_name = user_name
        self.password = password
        self.is_locked = is_locked