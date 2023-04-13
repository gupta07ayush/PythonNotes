# split the string into the list of strings
# then join the list of strings into a string based on delimiter - and ,

def split(str):
    print("Original string =",str)
    list_of_string = str.split(" ")
    print("String after split =", end="")
    return list_of_string
    
def myjoin(list_of_string):
    st = '-'.join(list_of_string)
    print("-".join(string.split()))
    print("List after join = ", end="")
    return st
    


if __name__== "__main__":
    string = 'Geeks for Geeks'
    
    mylist = split(string)
    print(mylist)
    
    myjoin = myjoin(string)
    print(myjoin)