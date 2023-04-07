mylist = [11,12,13,14,15]
total = 0

for i in range(0,len(mylist)):
    total = total + mylist[i]
print("total = ",total)


# Method 2
t = sum(mylist)
print(t)


# Method 3
s= [ i for i in mylist]
print(sum(s))