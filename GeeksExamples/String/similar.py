new = []

input = 'geeksforgeeks'

for i in input:
    if i not in new and input.count(i)>1:
        new.append(i)
print(" ".join(new))
