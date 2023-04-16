# Extract digits from tuple list

# Method 1

test = [(15, 3), (3, 9), (1, 10), (99, 2)]
print("Original list containing tuples are: \n",test)

x = ''

for i in test:
    for j in i:
        x += str(j)
res = list(map(int,set(x)))
print("All digits contained by list as tuple are; \n",res)