# Remove all duplicate words from a given sentence

s = "Python is great and Java is also great"
l = s.split()
k =[]

for i in l:
    if s.count(i) >=1 and i not in k:
        k.append(i)
print(s)
print(" ".join(k))



# Method 2
print(' '.join(dict.fromkeys(s.split())))

# Method 3
print(" ".join(set(s.split())))