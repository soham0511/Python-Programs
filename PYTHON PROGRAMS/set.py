a={1,3,7,68,1}
print(a)
#no repeated items ignores repeated items
#a={} #empty dictionary not empty set

#a=set() # empty set
#adding elements
a.add(9)
a.add(8)
#cannot add list and dictionary in set because list is hashable but tuple can be added
print(a)

#sets are unordered

#cannot access individual elements in a set
#a.remove(4)#removes 4 from set and throws an error if item is not rpesent in set

#a.pop returns am arbitary element and updates the set

#a.union(b) #union of set a and b
#a.intersection(b) #intersection of set a and b
