from abc import ABC, abstractmethod

# # نص باسطر متعددة
# print('''hi
# i am abdurhman
# thanks.''')
# int = 1
# str = "abdurhman"
# print(type(int)) # طباعة نوع المتغير
# # طرق لربط النصوص
# print("abdurhman" " " "sami")
# print("abdurhman" + "sami")
# print("abdurhman" + "sami")
# print(str[1:3]) # اقتطاع جزء من النص
# print(str[3:]) # اقتطاع جزء من النص الى نهايته
# print(len(str)) # طول النص , ملاحظة لا يمكن تغيير اي عنصر داخل النص

#تمرين استخراج الحرف الاول من بداية اسمك الاول + الحرف الاول من اسمك الثاني
# fristName = 'Abdurhman'
# lastName = 'Sami'
# print(fristName[0] + '.' + lastName[0])

# العامل الثلاثي
# age = int(input('place enter yiur age: '))
# if 17 < age < 61:
#     print('True')
# else:
#     print('False')
#يمكن اختصارها هكذا
# result = 'True' if 17 < age < 61 else 'False'
# print(result)


# # 07. القوائم Lists-----------------------------------------------------
# arr2 = [1,3,5,"and",6,True] # يمكن ان تشمل انواع متعددة لكن لا ينصح بذلك
# arr = [1,3,5,2] # يمكن ان تشمل انواع متعددة لكن لا ينصح بذلك
# print(arr[1:4])
# arr.append(1) # اضافة عنصر لاخر المصفوفة
# arr.insert(1,2) # اضافة عنصر في موضع معين من المصفوفة
# arr.pop(2) # حذف عنصر في موضع معين من المصفوفة
# arr.remove(1) # حذف قيمة عنصر معين
# print(arr.index(2)) # استخراج مكان العنصر
# print('and' in arr) # هل العتصر موجود في المصفوفة؟
# arr.sort() # الترتيب تصاعديا
# arr.sort(reverse=True) # الترتيب تنازليا
# print(arr)
# arr2.clear() # clear the array
# print(arr2)


# # 08. الصفوف Tuples ------------------------------------------------------------
# #طرق انشاء الصفوف
# arr = 1,2,3,4
# arr2 = (1,2,3,4)
# arr3 = 1,

# 09. القواميس Dictionaries-------------------------------------------------------
# dic = { 'ali': 2000 , 'sad': 2600, 'mohmmad': 1500}
# print(list(dic)) # طباعة المفاتيح
# del dic['ali'] # حذف مفتاح
# print(dic.get('mohmmad')) # get value
# print('sad' in dic) # التحقق من وجود مفتاح معين
# print(dic)


# # 10. الحلقات التكرارية----------------------------------------------------------
# for x in range(3,10,2): # اطبع من الرقم 3 الى 9 كل خطوة زود رقمين
#     print(x) 

# # 11. بنى List Comprehension----------------------------------------------------------
# arr = ['ahmed', 'mohammed', 'ali']
# arr2 = []
# for i in arr: # تغيير اول حرف في كل عنصر لحرف كبير 
#     if i[0] == 'a':
#         arr2.append(i.title())
# print(arr2)
# # يمكن اختصارها هكذا
# arr3 = [i.title() for i in arr if i[0] == 'a']
# print(arr3)
# # تمرين انشاء قائمة عبارو عن تربيع عناصر القائمة الاولى
# arr1_1 = [1,2,3,4,5]
# arr1_2 = [i*i for i in arr1_1]
# print(arr1_2)


# 12. الدوال Functions----------------------------------------------------------------
# def printNumbers(end, start=50): # لاحظ المعاملات ذات القيمة الافتراضبة نضعها في الاخير
#     """this is the function that prints the numbers"""  # هكذا يمكن اعطاء شرح لهذه الدالة ويظهر هذا الشرح عند وضع المواس غلى اسم الداله المستدعاه لتسهيل فهم وظيفة الدالة
#     for i in range(start, end):
#         print(i)
# printNumbers(100)


# # 13. حواشي الدوال Function Annotations ---------------------------------------------
# def printNumbers(end:int, start:int=50) -> float: # ليس هناك تاثير لهذه الحواشي على بايثون لكن تستخدم للتسهيل البرمجه وتقليل الاخطاء وتستخدم من طرف ثالث ايضا لكتابه التوثيق مثلا يمكنك مثلا اضافة نوع متغير غير صحيح ستحد رساله تقوم بتنبيهك
#     """this is the function that prints the numbers"""  # هكذا يمكن اعطاء شرح لهذه الدالة ويظهر هذا الشرح عند وضع المواس غلى اسم الداله المستدعاه لتسهيل فهم وظيفة الدالة
#     for i in range(start, end):
#         print(i)
#     return 2.00
# print(printNumbers(60))


# # 14. المزخرفات Decorators - الجزء الأول-----------------------------------------------
# # يمكن استخدام الدوال داخل دوال اخرى كمعاملات هكذا
# def printName():
#     return 'Ahmed'
# def printNumbers(end:int, operation, start:int=50) :
#     for i in range(start, end):
#         print(i , ' ' , operation)
#     return 2.00
# print(printNumbers(60, printName()))
# #===============================
# def Plus(x):
#     return x+1
# def Minus(x):
#     return x-1
# def Number(x, operation) :
#     return 2*operation(x)
# print(Number(5, Plus))
# #يمكن ايضا ان ترجع الداله داله اخرى كما هنا
# def Plus():
#     return print('Plus')
# def Minus():
#     return print('Minus')
# def Number() :
#     return Plus
# Number()() #هنا رجعت الدالة اسم داله اخرى ثم وضعتا اقواس اخرى لنستدعي الداله المرجعه ويمكن تحزينها في متغير ايضا
# x = Number()
# x()

# 15. المزخرفات Decorators - الجزء الثاني
# يحتاج مراجعة فهمته لكن يحتاج ترسيخ
# https://academy.hsoub.com/courses/computer-science/oop/python-basics/15-%D8%A7%D9%84%D9%85%D8%B2%D8%AE%D8%B1%D9%81%D8%A7%D8%AA-decorators-%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-%D8%A7%D9%84%D8%AB%D8%A7%D9%86%D9%8A-r3419/


# 16. الوحدات Modules 
# يجدر التنبيه انه بامكاننا اسنتخدام امر الاستيراد ابضا داخل سطر الاوامر لاستدعاء داله معينه داخل ملف معين


# # 04. تعريف الأصناف والكائنات Declaring Classes and Objects----------------------
# class Employee: # تعريف كائن جديد
#     def __init__(self, name, salary, age):
#         self.name = name
#         self.salary = salary
#         self.age = age
#     def print_info(self):
#         print ("Name: " + self.name + " salary: " + str(self.salary) + " age: " + str(self.age))
# ahmed = Employee('ahmed', 3500, 30)
# ahmed.print_info()
# # يمكن اضافة خصائص جديدة في اي نسخة من الكائن بحث تكون خاصه بهذه النسخة فقط
# class person:
#     pass
# ali = person()
# ali.name = 'ali'
# print(ali.name)

# 05. خصائص وتوابع الأصناف Class Properties and Methods ----------------------------------------------------------------
# class Employee:
#     totall = 0 # خصائص خاصه بالصنف نفسه وليس الكائنات المشتقة منه
#     salary_raise = 1.5

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.__salary = salary # وضعنا الشرطتين السفليتين لمنع التعديل على العنصر الا من داخل الصنف فقط
#         self.age = age
#         Employee.totall += 1 
    
#     def get_info(self):
#         return f"Name: {self.name} Age: {self.age} salary: {self.__salary}"

#     @classmethod # هذه العلامة تدل ان هذه الداله خاصه بالصنف فقط وليست خاصه بالكائنات
#     def change_raise(cls, amount):
#         cls.salary_raise = amount
        
#     @classmethod
#     def from_string(cls, string):
#         name, age, salary = string.split('-')
#         salary = int(salary)
#         age = int(age)
#         return cls(name, age, salary) # هتا ارجعنا قيم العوامل الخاصة بانشاء كائن جديد من هذا الصنف
    
#     @staticmethod # هذه العلامة تدل ان هذه الداله ليس لها اي علاقة بالصنف او الكائنات الخاصة به علما اننا لو ازلناها فلن يكون هناك تاثير فقط للتسهيل
#     def  printHello():
#         print("Hello")

# # ali = Employee('ali', 20, 2500)
# # print(ali.get_info())
# # ali.printHello()
# # ali = ali.from_string('ahmed-23-1500')
# # print(ali.get_info())
# # del ali # delete object

# # 08. التغليف Encapsulation ----------------------------------------------------------------
# # لم افهم من الدقيقة 6:40
# # https://academy.hsoub.com/courses/computer-science/oop/oop/08-%D8%A7%D9%84%D8%AA%D8%BA%D9%84%D9%8A%D9%81-encapsulation-r3428/


# # 09. الوراثة Inheritance ----------------------------------------------------------------
# class Manager(Employee):
#     def __init__(self, name, age, salary, employees ):
#         super().__init__(name, age, salary) # نبين ان هذه الخواص تتبع الصنف الاساس الموروث منه
#         self.employees = employees

#     def get_employees(self):
#         print ("Employees:")
#         print ("="*20)
#         employees_list = []
#         for num, employee in enumerate(self.employees): # enumerate هذه تجلب رقم الدورة
#             employees_list.append(f"{num + 1}. {employee.get_info()}")
#         return '\n'.join(employees_list)

# # تدريب الوراثة انشئ صنف مبرمج ومشاريع----------------------------
# class Programmer(Employee):
#     def __init__(self,name, age, salary, lang, projects):
#         super().__init__(name, age, salary)
#         self.lang = lang
#         self.projects = projects

#     def get_ptojects(self):
#         print("projects:")
#         print("-"*20)
#         projects_list = []
#         for num, project in enumerate(self.projects):
#             projects_list.append(f"{num + 1}. {project.get_info()}")
#         return '\n'.join(projects_list)

# class project:
#     def __init__(self, name, description, days, done):
#         self.name = name
#         self.description = description
#         self.days = days
#         self.done = done
#     def get_info(self):
#         return f"name: {self.name}, description: {self.description}, days: {self.days}, done: {self.done}"

# pro1 = project('project1', 'description1', 12, True)
# pro2 = project('project2', 'description3', 3, False)
# pro3 = project('project3', 'description3', 15, True)
# ali = Programmer('ali', 20, 2500, 'python', [pro1, pro2, pro3])
# print(ali.get_info())
# print(ali.get_ptojects())


# 10. التجريد Abstraction ----------------------------------------------------------------
# تدريب أنشئ صنفًا جديدًا وليكن Accountant مثلًا يرث من الصنف Employee. أضف إلى هذا الصنف خصائص جديدة وتوابع جديدة، ولا تنس إنشاء اﻷصناف الموروثة من الصنف Employee.
class Employee(ABC):
    totall = 0 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profile = None # يمكن اضافة خصائص جديدة هكذا لنقوم بربطها مع صنف اخر مثلا كما في هذا المثال
        Employee.totall += 1 
    
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass  

    @classmethod
    @abstractmethod
    def from_string(cls, string):
        pass

class Accountant(Employee):
    def __init__(self, name, age, salary, groups=None):
        super().__init__(name, age)
        self.salary = salary
        if groups is None:
            groups = []
        self.groups = groups
    
    def get_info(self):
        return f"Name: {self.name} \nage: {self.age} \nsalary: {self.salary} \ngroups: {self.groups}"
    
    def calculate_salary(self):
        pass
    
    @classmethod
    def from_string(cls, string):
        name, age, salary, groups = string.split('-')
        salary = int(salary)
        age = int(age)
        groups = groups.split(',')
        return cls(name, age, salary, groups)
        
    def assign_groups(self, group):
        self.groups.append(group)

ali = Accountant.from_string('ali-23-2300-group2,group5,group8')
# ali = Accountant('ali', 32, 3333)
print(ali.get_info())



# 13. التركيب Composition ----------------------------------------------------------------
class Profile:
    def __init__(self, address, phone, married, country, city):
        self.address = address
        self.phone = phone
        self.married = married
        self.country = country
        self.city = city

ali = Accountant.from_string('ali-23-2300-group2,group5,group8')
profileAli = Profile("addr","0050000", False, "saudi arabe", "ryide")
ali.profile = profileAli
print(ali.profile.phone)