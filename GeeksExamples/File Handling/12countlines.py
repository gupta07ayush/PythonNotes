# Count number of line

file = open('file1.txt', 'r')
counter = 0

content = file.read()
mylist = content.split('\n')

for i in mylist:
    if i:
        counter += 1

print(f"The number of lines in this file = {counter} ")
