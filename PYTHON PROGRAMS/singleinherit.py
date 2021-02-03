class Employee:
    company="Google"
    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    language="Python"
    def getlanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("This is an Programmer")

e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()#Overrides the shoeDetails() of Employee
#print(p.company)