# convert key-value list to flat dictionary

test = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
res = {test['month'][i]: test["name"][i] for i in range(len(test['month']))}
print(test)
print(res)