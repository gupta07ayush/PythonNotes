# Read file letter by letter

with open("textobject.txt", 'r') as file:
    for word in file:
        for letter in word:
            print(letter)
