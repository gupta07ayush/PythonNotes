# Python3 code to demonstrate working of
# Convert Snake case "to Pascal case
# Using title() + replace()

test = 'geeks_for_geeks_is_best'
test = test.title()
new = test.replace("_", "")
print(new)