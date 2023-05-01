# Append content of one text file to another
firstfile = 'file1.txt'
secondfile = 'textobject.txt'

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('first file before appending: ', f1.read())
print('second file before appending: ', f2.read())

f1.close()
f2.close()

# opening first file in append mode and second file in read mode
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

# appending the contents of the second file to the first file
f1.write(f2.read())

# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

# printing the contents of the files after appendng
print('first file after appending: ', f1.read())
print('second file after appending: ', f2.read())

f1.close()
f2.close()
