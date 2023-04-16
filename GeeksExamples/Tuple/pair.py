# All pair combinations of 2 tuples
# Method 1 using list comprehension

test1 = (4, 5)
test2 = (7, 8)

print(test1,test2)

res = [ (a,b) for a in test1 for b in test2 ]
res = res + [ (a,b) for a in test2 for b in test1 ]

print("Output: \n", res)