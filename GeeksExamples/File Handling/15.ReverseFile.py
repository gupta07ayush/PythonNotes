# Python program to reverse the content of a file and store it in another file

# This reversing can be performed in two types:
# 1. Full reversing
# 2. Word to word reversing

# 1. Full Reversing
f1 = open('reverse.txt', 'w')

with open("writefile.txt", 'r') as myfile:
    data = myfile.read()

# for full reversing we will store the value of data
# into new variable data1 in a reverse order using slicing [start: end: step],
# where in step when passed -1 will reverse the string.

data1 = data[::-1]

f1.write(data1)
f1.close()


# 2. Word by word reversing
f2 = open('reverse2.txt', 'w')

with open('writefile.txt', 'r') as myfile:
    data = myfile.readlines()

# we will just reverse the array using following code
data2 = data[::-1]

f2.writelines(data2)
f2.close()
