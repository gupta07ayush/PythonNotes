# sort Dictionary key and values list

# Method 1
test = {'gfg': [7, 6, 3],
        'is': [2, 10, 3],
        'best': [19, 4]}

res = dict()
for key in sorted(test):
    res[key] = sorted(test[key])
print(test)   
print(res)