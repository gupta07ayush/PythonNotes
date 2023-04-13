# Check if a given string is binary or not

def check(string):
    str =set(string)
    binary = {"0","1"}
    zero = {0}
    one = {1}
    
    if str == binary or str == zero or str==one:
        print("Please give input in english not in binary.")
    else:
        pass
string1 = "101001100101010"
check(string1)
print()


def check2(string):
    t = '01'
    count = 0
    
    for char in string:
        if char not in t:
            count = 1
            break
        else:
            pass
        
    if count:
        print("Binary")
    else:
        print("Not binary")
    
check2(string1)