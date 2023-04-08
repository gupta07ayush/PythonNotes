# print duplicates from a list of integers

# Method 1: Using a single for loop
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
unique = []
duplicate = []

for i in lis:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print(lis)
print("Duplicate", duplicate)
print("Unique",unique)
print()

# Method 2 using count()
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
new = []
for i in list:
    n= list.count(i)
    if n>1:
        if new.count(i) == 0 :
            new.append(i)
print(list)
print("Unique ",new)
print()



# Method 3: Using in, not in operators and count() method
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(lis)
print(y)