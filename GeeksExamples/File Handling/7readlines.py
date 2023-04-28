# readline() reads a single line and returns it as a string.
# whereas readlines() read the content of a file, line by line and returns them as a list of strings.

with open("textobject.txt", 'r') as file:
    data = file.readlines()
    print(data)
