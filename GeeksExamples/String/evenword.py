string ="This is a python language and I love my father"
def even(n)
    n = n.split()
    for i in n:
        if len(i)%2==0:
            return i 
        
print(even(string))

# Method 2 using list comprehension
y= [x for x in n if len(x)%2==0]
print(y)
