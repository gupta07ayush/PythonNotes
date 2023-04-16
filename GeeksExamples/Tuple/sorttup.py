# Python Program to sort a list of tuples by second item

# Using bubble sort

def sort(tup):
    lst = len(tup)
    for i in range(0,lst):
        for j in range(0, lst-i-1):
            if tup[j][1] > tup[j+1][1]:
                temp = tup[j]
                tup[j] = tup[j+1]
                tup[j+1] = temp
    return tup
    
    
tup = [('for', 24), ('is', 10), ('Geeks', 28),
       ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
 
print(sort(tup))
print()


# Method 2
def tuplist(tup):
    tup.sort(key = lambda x : x[1])
    return tup

tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
 
# printing the sorted list of tuples
print(tuplist(tup))