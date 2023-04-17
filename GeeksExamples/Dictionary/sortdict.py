# sorted() with lamdba

list = [{"name": "Nandini", "age": 23},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(sorted(list, key= lambda i: i['age']))
print('\r')

# if you want to sort by both age and name.
print(sorted(list, key =lambda i: (i['age'], i['name'])))
print('\r')

# sort in reverse order
print(sorted(list, key=lambda i:i['age'], reverse=True))
