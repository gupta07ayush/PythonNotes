# Flatten tuple of list to tuple

# Method 1 using append
test = ([5], [6], [3], [8]) 
res = []
for i in test:
    for j in i:
        res.append(j)
print(tuple(res))
        
    
# Method 2 using extend
new = []
for i in test:
    new.extend(i)
print(tuple(new))