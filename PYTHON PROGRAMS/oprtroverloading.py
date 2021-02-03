class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Let's add")
        return self.num+num2.num
    def __mul__(self,num2):
        print("Let's multiply")
        return self.num*num2.num

n1=Number(3)
n2=Number(5)
n1+n2
n1*n2
sum=n1+n2
prod=n1*n2
print(sum)
print(prod)