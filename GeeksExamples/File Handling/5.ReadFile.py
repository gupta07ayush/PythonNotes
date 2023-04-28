# Read only first line using readline()

with open("textobject.txt", 'r') as file:
    line = file.readline()
    print(line)  # This will print only one line
