class Person:
    country="INDIA"
    def __init__(self):
        print("Initializing Person")
    def breathe(self):
        print("I am Breathing...")

class Employee(Person):
    company="OYO"
    def __init__(self):
        super().__init__()
        print("Initializing Employee")
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def breathe(self):
        super().breathe()
        print("I am an Employee so I am luckily breathing....")
        
class Programmer(Employee):
    company="UPWORK"
    def __init__(self):
        #super().__init__()
        print("Initializing Programmer")
    def getSalary(self):
        print("No salary to programmer")
    def breathe(self):
        super().breathe()
        print("I am an Programmer so I am breathing + + ....")

# p=Person()
# p.breathe()
# e=Employee()
# e.breathe()
pr=Programmer()
pr.breathe()
# print(pr.company)
# print(pr.country)
