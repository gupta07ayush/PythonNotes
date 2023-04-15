#find the size of a tuple in python

# method 1 using getsizeof() function
import sys
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

a = sys.getsizeof(Tuple1)
b = sys.getsizeof(Tuple2)
c = sys.getsizeof(Tuple3)

print(a,"bytes")
print(b,"bytes")
print(c,"bytes")
print()




# Method 2 using inbuilt __sizeof__() method
# Python also has an inbuilt __sizeof__() method to determine the space allocation of an 
# object without any additional garbage value.

d = Tuple1.__sizeof__()
e = Tuple2.__sizeof__()
f = Tuple3.__sizeof__()

print(d,"bytes")
print(e,"bytes")
print(f,"bytes")
