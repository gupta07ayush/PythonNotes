# split the string into the list of strings
# then join the list of strings into a string based on delimiter - and ,

s = "Geeks for Geeks"
print(s)

split = s.split(" ")
print(split)

join = "-".join(split)
join2 = "-".join(s.split())
print(join)
print(join2)