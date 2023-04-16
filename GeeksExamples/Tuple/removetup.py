# Remove tuple of Length K
test = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

# Method 1
k=1
new = []
for i in test:
    if len(i) != k:
        new.append(i)
print(new)


# Using List comprehension
res = [x for x in test if len(x) != k]
print(res)