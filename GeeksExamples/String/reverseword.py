def reverse_string(s):
    print("Original string is:",s)
    s = s.split()
    s = s[::-1]
    new_str = " ".join(s)
    print("Reversed words are:",new_str)

str = "My name is Ayush"
reverse_string(str)

string= "I live in Bhopal"

s = string.split()[::-1]
new = []
for i in s:
    new.append(i)
print(" ".join(new))