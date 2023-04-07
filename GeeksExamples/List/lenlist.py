
# Ways to find length of list in python

# Method 1
mylist = [1,2,3,4,5]
length = len(mylist)
print(length)


# Method 2
count = 0
for i in mylist:
    count += 1
print(count)



# Method 3
from operator import length_hint
length2 = length_hint(mylist)
print(length2)


# Method 4
for i,a in enumerate(mylist,1):
    print(i,a)
    
    
