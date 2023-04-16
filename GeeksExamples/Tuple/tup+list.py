# concatenate list into tup



test_list = [5, 6, 7]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing tuple
test_tup = (9, 10)
 
# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)
test_tup += tuple(test_list)
print(test_tup)




