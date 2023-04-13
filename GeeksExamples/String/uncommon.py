# find a list of uncommon words

def uncommon(a,b):
    a = a.split()
    b = b.split()
    x = []
    for i in a:
        if i not in b:
            x.append(i)
    for i in b:
        if i not in a:
            x.append(i)
    x= list(set(x))
    return x 
a = "Geeks for Geeks"
b = "Learning from Geeks for Geeks"

print(uncommon(a,b))