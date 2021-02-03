class Employee:
    company="VISA"
    eCode=3124212
class Freelancer:
    company="UPWORK"
    level=4
    def upgradeLevel(self):
        self.level+=1


class Programmer(Freelancer,Employee):#Priority of the class which is named first is given priority
    name="Soham"

p=Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)