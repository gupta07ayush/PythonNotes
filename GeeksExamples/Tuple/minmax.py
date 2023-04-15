# make a function which takes a tuple as input and returns a tuple
# containing only two values min and max of the input tuple

tup = (3,7,1,18,9)

def minx(x):
    newlist = []
    y = sorted(x)
    newlist.append(y[0])
    newlist.append(y[-1])
    print(tuple(newlist))
minx(tup)
        