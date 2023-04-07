# Multiply the all elements in the list


# Method 1
r = 1
mylist = [1,2,3,4,5]
for i in mylist:
    r = r * i
print(r)


# method 2
import numpy
result = numpy.prod(mylist)
print(result)

