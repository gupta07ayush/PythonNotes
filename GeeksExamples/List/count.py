# Count occurrences of an element in a list

# method 1 using loop
def countx(list,x):
    count =0
    for i in list:
        if i==x:
            count+=1
    return count
list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,countx(list, x)))

print(countx(list,x))




# Method 2 using count()
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8

print(lst.count(x))
