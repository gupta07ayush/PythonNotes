# Python code to count number of unique matching characters in a pair of strings

def count(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    
    matched = set1 & set2
    print("No of matching characters are: "+ str(len(matched)))
    
str1 = 'aabcddekll12@'  # first string
str2 = 'bb2211@55k'     # second string
 
# call count function
count( str1 , str2 )