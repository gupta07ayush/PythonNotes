str1 = "geeksforgeeks"

def rem_dup(str):
    new = ""
    for i in str:
        if i not in new:
            new += i
        else: 
            pass
    return  new
print(rem_dup(str1))
