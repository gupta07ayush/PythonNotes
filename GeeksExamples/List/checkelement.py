# check if element exists in list 

import random
mylist = random.sample(range(10,50),25)
print(mylist)
print()

if 17 in mylist:
    print(17,"is present")
else:
    print(f"17 is not present")
   
    
e = random.randint(10,50)
if e in mylist:
    print(e,"is present")
else:
    print(e,"is not present")
    

from random import sample
f = sample(mylist,1)
if f[-1] in mylist:
    print(f[-1],"yes")
    

# Method 2
for i in mylist:
    if i==21:
        print(21,"is present")
else:
    print(21, "is not present")
    



# Method 3 using count

a = mylist.count(e)
if a == 1:
    print(e,"is present")
else:
    print(e,"is not present")