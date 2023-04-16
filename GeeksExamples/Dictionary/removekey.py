# ways to remove a key from dictionary

# Method 1 using del
test = {"Arushi": 22, "Mani": 21, "Haritha": 20}
print(test)
del test['Mani']
print(test)


# Method 2 using pop
test = {"Arushi": 22, "Mani": 21, "Haritha": 20}
test.pop('Mani')
print(test)
x = test.pop('Arushi') # x will give the value of deleted key element 


# Method 3 using dict comprehension
test = {"Arushi": 22, "Mani": 21, "Haritha": 20}
new = {key:val for key, val in test.items() if key != 'Mani'}



# Method 4
test = {"Arushi": 22, "Mani": 21, "Haritha": 20}
adict = {key:test[key] for key in test if key != 'Mani'}
print(adict)


# Method 5
test = {"Arushi": 22, "Mani": 21, "Haritha": 20}
y = {}
for key,value in test.items():
    if key != "Mani":
        y[key] = value
print(y)

