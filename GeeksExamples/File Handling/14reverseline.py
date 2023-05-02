# Python Program to reverse a single line of a text file
f = open('file1.txt', 'r')
lines = f.readlines()

f.close()

choice = 1
line = lines[choice].split()

reversed = " ".join(line[::-1])

lines.pop(choice)
lines.insert(choice, reversed)

u = open('writefile.txt', 'w')

u.writelines(lines)
u.close()
