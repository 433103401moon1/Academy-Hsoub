# الوراثة المتعددة
#  https://academy.hsoub.com/courses/computer-science/oop/oop/11-%D8%A7%D9%84%D9%88%D8%B1%D8%A7%D8%AB%D8%A9-%D8%A7%D9%84%D9%85%D8%AA%D8%B9%D8%AF%D8%AF%D8%A9-multiple-inheritance-r3431/

from Employee import Employee #, Freelancer
from Manager import Manager, FreelancerManager
from Accountant import Accountant
from Programmer import Programmer , FreelancerProgrammer
from Payments import *
from Roles import *
from Profile import *

if __name__ == '__main__':
    profileAli = Profile("addr","0050000", False, "saudi arabe", "ryide")
    ali = Manager("kalid", "mohamed", 3000)
    # ahmed = FreelancerManager("ahmed", "mohamed", [ali, kalid], 100, 2)
    ali.profile = profileAli
    print(ali.profile.address)
    # print(ahmed.get_ptojects())
    # ahmed.assign_project("pro111")
    # print(ahmed.get_ptojects())
    # ahmed = FreelancerProgrammer("ahmed", "mohamed", "JS", ["pro1","pro5"], 100, 2)
    # print(ahmed.get_info())
    # print(ahmed.get_ptojects())
    # ahmed.assign_project("pro111")
    # print(ahmed.get_ptojects())
# ----------------------------------------------------------------
# ahmed = Manager("ahmed", "ali", 3333 )
# print(ahmed.get_info())
# ahmed = Freelancer("ahmed", "ali", 100, 3 )
# print(ahmed.get_info())
# print(ahmed.get_info())
