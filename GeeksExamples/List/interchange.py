# Python program to interchange first and last elements in a list
#Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# method 1 using temp 
mylist = [12, 35, 9, 56, 24]
print("input list",mylist)

temp = mylist[0]
mylist[0] = mylist[-1]
mylist[-1] = temp

print("Output list",mylist)


# Method 2 using shorcut swap 
print()
myl = [24, 35, 9, 56, 12]
print(myl)
myl[0], myl[-1] = myl[-1], myl[0]
print(myl)
print()


# Approach #4: Using * operand. 
# This operand proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name. 

def swap(list):
    start, *middle, end = list
    list2 = [end, *middle, start]
    return list2
newlist = [12, 35, 9, 56, 24]
print(newlist)
print(swap(newlist))
print()

#Approach #5: Swap the first and last elements is to use the inbuilt function list.pop(). Pop the first element and store it in a variable. Similarly, pop the last element and store it in another variable. Now insert the two popped element at each other’s original position. 
def swapList(list):
     
    first = list.pop(0)  
    last = list.pop(-1)
     
    list.insert(0, last) 
    list.append(first)  
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))