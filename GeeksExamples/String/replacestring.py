str = "Ayush is a good boy. He is also a good cook and he is a good philosopher too."
word = ["good"]
replace = "awesome"

for i in word:
    test = str.replace(i,replace)
    
print(test)