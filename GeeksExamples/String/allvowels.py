# Program to accept the strings which contains all vowels. 

def check(s):
    s = s.lower()
    vowels = set("aeiou")
    dict = set({})
    
    for char in s:
        if char in vowels:
            dict.add(char)
        else:
            pass
    
    if len(dict) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")

# Driver code
if __name__ == "__main__":
    string = "aioeiou"
    
    check(string)
