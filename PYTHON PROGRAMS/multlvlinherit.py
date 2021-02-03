class Person:
    country="INDIA"
    def breathe(self):
        print("I am Breathing...")

class Employee(Person):
    company="OYO"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def breathe(self):
        print("I am an Employee so I am luckily breathing....")
        
class Programmer(Employee):
    company="UPWORK"
    def getSalary(self):
        print("No salary to programmer")

p=Person()
e=Employee()
pr=Programmer()
pr.breathe()
print(pr.company)
print(pr.country)
