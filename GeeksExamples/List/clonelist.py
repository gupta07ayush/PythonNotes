# Cloning or copying a list

# Method 1 using slicing
mylist = [4, 8, 2, 10, 15, 18]
mylist1 = mylist[:]
print(mylist)
print(mylist1)
print()


# Method 2 using extend
mylist = [4, 8, 2, 10, 15, 18]
mylist2 = []
mylist2.extend(mylist)
print(mylist)
print(mylist2)
print()


# Method 3 using assignment operator
# There is an issue with this method if you modify in the new list then the old list is also modified due to the new list is referencing
mylist = [4, 8, 2, 10, 15, 18]
mylist3 = mylist
print(mylist)
print(mylist3)
print()


# method 4 using shallow copy
import copy

mylist = [4, 8, 2, 10, 15, 18]
mylist4 = copy.copy(mylist)
print(mylist)
print(mylist4)
print()



# Method 5 using list comprehension
mylist = [4, 8, 2, 10, 15, 18]
mylist5 = [x for x in mylist]
mylist = [4, 8, 2, 10, 15, 18]
print(mylist)
print(mylist5)
print()



# method 6 using copy() method
mylist = [4, 8, 2, 10, 15, 18]
mylist6= mylist.copy()
print(mylist)
print(mylist6)
print()

# Method 7 Deep copy
# This takes around 10.59 seconds to complete and is the slowest method of cloning. 
import copy
mylist = [4, 8, 2, 10, 15, 18]
mylist7 = copy.deepcopy(mylist)
print(mylist)
print(mylist7)
print()
