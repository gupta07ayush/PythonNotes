# Convert a list of tuples into dictionary

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
res = {}

for key,value in tups:
    res.setdefault(key, value)
print(tups)
print()
print(res)
print()

# Method 2
di = {}
di = dict(tups)
print(di)