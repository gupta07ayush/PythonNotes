# keys associated with values in dictionary

test = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]}

result = {}
for key, val in test.items():
    for ele in val:
        if ele in result:
            result[ele].append(key)
        else:
            result[ele] = [key]
print(test)
print()
print(result)