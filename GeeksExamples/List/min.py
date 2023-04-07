# find smallest number in a list



#method 1
import random 
mylist = random.sample(range(20,50),10)
print(mylist)
print(min(mylist))



#method 2
mylist.sort()
print(mylist[0])


#method 3
mylist.sort(reverse=True)
print(mylist[-1])


# method 4
import numpy
print(numpy.min(mylist))



# method 5
list2 =  [5,2,3,2,5,4,7,9,7,10,15,68]
print(list2)
list3 = set(list2)
print(min(list3))
