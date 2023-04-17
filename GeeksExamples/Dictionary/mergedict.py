# merging two dictionary

def merge(dica,dicb):
    return dicb.update(dica)

dica = {'a': 10, 'b': 8}
dicb = {'d': 6, 'c': 4}

print(merge(dica,dicb))
print(dicb)


#method 2
def mer(a,b):
    result = {**a, **b}
    return result

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = mer(dict1, dict2)
print(dict3)


# Method 3
def Merge(dict1, dict2):
    res = dict1 | dict2
    return res
      
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)
 