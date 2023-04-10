n="This is a python language and I love my father"
n = n.split()
for i in n:
    if len(i)%2==0:
        print(i)


# Method 2 using list comprehension
y= [x for x in n if len(x)%2==0]
print(y)