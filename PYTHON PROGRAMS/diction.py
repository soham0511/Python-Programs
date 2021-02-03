dict={
    "fast":"In a quick manner",
    "soham":"Hackerrank Gold Medalist",
    "marks":[1,2,4],
    "another dict":{"Soham":"Pro Coder"}
}
#mutable and inputing two valus for same key overrides

#Dictionary Methods 
print(dict["fast"])
print(dict["soham"])
print(dict["another dict"]["Soham"])
print(dict.keys())
print(dict.values())
print(dict.keys())
#updating dictionary
newdict={"vivek":"friend"}
dict.update(newdict)
print(dict)

print(dict.get("soham"))#return null if key is not present in dictionary