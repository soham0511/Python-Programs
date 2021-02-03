class Employee:
    company="HP Gas"
    salary=32000
    salarybonus=1500
    
    @property  #getter
    def totalSalary(self):
        return self.salary+self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val-self.salary
e=Employee()
print(e.totalSalary)
e.totalSalary=35000
print(e.salary)
print(e.salarybonus)
