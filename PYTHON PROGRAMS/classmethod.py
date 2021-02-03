class Employee:
    company="TATA"
    salary=1000
    location="Delhi"
    # def salaryupdate(self,sal):
    #     self.salary+=sal

    # def salaryupdate(self,sal):
    #     self.__class__.salary+=sal
    
    @classmethod
    def salaryupdate(cls,sal):
        cls.salary+=sal


# e=Employee()
# print(e.salary)
# e.salaryupdate(356)#changes instance of the class variable without super()
# print(e.salary)
# print(Employee.salary)#unaffected by update

e=Employee()
print(e.salary)
e.salaryupdate(356)#changes th class variable
print(e.salary)
print(Employee.salary)#affected by update