def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Soham is a Hackerrank gold Medalist       "
n = remove_and_split(this, "Soham")
print(n)
# print(this)
# print(this.strip())
