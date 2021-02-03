#lists can update the values
a=[1,2,"Soham",57,9.89]
print(a)
print(len(a)) #length of list
print(a[3])
print(type(a))
print(a[0:3]) #list slicing

#tuples cannot update values of tuples
t=(1,2,0)
#t1=() #Empty Tuple
#t2=(1) #Wrong way to define tuple
#t3=(1,) #Defining a tuple with single element
print(t[0])