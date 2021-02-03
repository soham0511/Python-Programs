# def percent(marks):
#     sum=0
#     for i in marks:
#         sum+=i
#     return sum/len(marks) 

# marks1=[12,56,78,99,100]
# marks2=[14,56,89,99,55]
# percentage1=percent(marks1)
# percentage2=percent(marks2)
# print(percentage1)
# print(percentage2)

# def greet(name="Stranger"):
#     print("Good Day "+name)
# greet()#default argument used   
# greet("Soham")
# greet("Vivek")

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input("Enter the number "))))