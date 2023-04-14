from itertools import permutations

def new(str):
    list = permutations(str)
    print(list)
    
    for i in list:
        print(''.join(i))
    
s = "AYUSH"    
new(s)
