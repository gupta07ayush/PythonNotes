# readline() gives you only first line
# We have to iterate to get all the lines

with open("textobject.txt", 'r') as file:
    for lines in file:
        print(lines)
    print("*****End of File*****\n")


# or print readline() n times to print n lines
with open("textobject.txt", 'r') as file:
    for i in range(2):
        # prints only two line
        print(file.readline())
