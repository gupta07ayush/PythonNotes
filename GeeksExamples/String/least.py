# print least frequent character in string

str = "geeksforgeeks"
mydict = {}

for i in str:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1
print(mydict)

result = min(mydict, key= mydict.get)
print(result)


# method 2
from collections import Counter

res = Counter(str)
res = min(res, key = res.get)
print(res) 
print(type(res))