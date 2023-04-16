# Python program to find sum of all items in a dictionary

# Method 1
def ret(mydict):
    mylist = []
    for i in mydict:
        mylist.append(mydict[i])
    return sum(mylist)
        
        
dict = {'a':100, 'b':200, 'c':300, 'd':400}
a = ret(dict)
print(a)



# Method 2
def returnsum(mdict):
    sum = 0
    for i in mdict.values():
        sum = sum + i
    return sum
b = returnsum(dict)
print(b)


# Method 3

def func(mydict):
    sum = 0
    for i in mydict:
        sum = sum + mydict[i]
    print(sum)
func(dict)
    

# Method 4
x = sum(dict.values())
print(x)


# Method 5 Using List comprehension
z = [dict[i] for i in dict]
print(sum(z))