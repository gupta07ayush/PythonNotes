with open("new.txt", 'a') as f:
    print("There are many Methods of TextIOWrappter class.", file=f)
    a = 'Ayush'
    b = "Gupta"
    print(a, b, file=f)


mydict = {
    "a": 1,
    "b": 2,
}

with open('myfile.txt', 'a') as fd:
    print(mydict, file=fd)

    c = {"c": 3}
    print(c, file=fd)
