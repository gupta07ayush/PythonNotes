# Maximum of two numbers in Python3
# Given two numbers, write a Python code to find the Maximum of these two numbers.

a,b = 5,18

# Method 1
def maximum(a,b):
    if a==b:
        print("Equal numbers.")
    elif a>b:
        print(a)
    else:
        print(b)
maximum(a,b)



#Method 2
print(max(a,b))


# Method 3
# Ternery operator
maxx = a if a>= b else b
print(maxx)


# List comprehension
y = [ a if a>=b else b]
print(y)


# sort() Method
x = [a,b]
x.sort()
print(x[-1])