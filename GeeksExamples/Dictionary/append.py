# Append dictionary keys and values

# method 1
test = {'Gfg': 1, "is":3, 'Best':2}
print(test)
res = list(test.keys()) + list(test.values())
print(res)


# Method 2
a = list(test.keys())
b = list(test.values())
a.extend(b)
res =a 
print(a)