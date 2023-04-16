# min and max k elements in Tuple

# Method   1
test = (5,20,3,7,6,8,11,44,32,89)
print(test,"test tuple")

k = 2
res = []

test = list(sorted(test))
#print(test)

for i,j in enumerate(test):
    if i<k or i>=len(test) - k:
        res.append(j)
print(tuple(res))



# Method 2 

tup = (5,20,3,7,6,8,11,44,32,89)
temp = list(sorted(tup))

result = temp[:k] + temp[-k:]
print(tuple(result))
