str1 = "geeksforgeeks"

new = ""
def rem_dup(str):
    for i in str:
        if i not in new:
            new += i
        else: 
            pass
    return  new
print(rem_dup(str1))
