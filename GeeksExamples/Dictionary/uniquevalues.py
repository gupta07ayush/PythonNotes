# Extract unique values of a dictionary

# Method 1 using list comprehension
test = {'gfg': [5, 6, 7, 8],
        'is': [10, 11, 7, 5],
        'best': [6, 12, 10, 8],
        'for': [1, 2, 5]}
res = sorted({ele for val in test.values() for ele in val})
print(res)


# Method 2
x = [ ]
for i in test.keys():
    x.extend(test[i])
x = list(set(x))
print(x)

