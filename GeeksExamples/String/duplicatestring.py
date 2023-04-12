str = "geeksforgeeks"
new = ""
for i in str:
    if i not in new:
        new = new + i      
print(new)