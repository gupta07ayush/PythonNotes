# Words Frequency in String
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
 
test_str = 'Gfg is best Geeks are good and Geeks like Gfg'
print(test_str)

y = {key:test_str.count(key) for key in test_str.split()}
print(y)