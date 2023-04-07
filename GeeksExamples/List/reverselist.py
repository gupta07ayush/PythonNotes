# reverser list

mylist = [10,11,12,13,14,15]
print(mylist)
mylist.reverse()
print(mylist)
mylist = list(reversed(mylist))
print(mylist)


# Method 2
newlist = []
for i in mylist:
    newlist.insert(0,i)
print(newlist)



# Method 3
list2 = newlist[::-1]
print(list2)