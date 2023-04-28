# Read file word by word
with open('textobject.txt', 'r') as file:
    for line in file:
        for word in line.split():
            print(word)
