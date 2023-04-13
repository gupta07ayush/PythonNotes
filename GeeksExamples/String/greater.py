# Python program to find all string which are greater than
# given length k

def string(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string

k = 3
str = "geeks for geeks is very good website"
print(string(k,str))


# Method 2 
sentence = "hello geeks for geeks is computer science portal"
k = 4

y = [word for word in sentence.split() if len(word) > k]
print(y)