# Python program to find difference between current time 
# and given time

# Approch:
# 1. convert both time into minutes
# 2. find the difference in minute
# 3. if difference is 0, 'Both time are same'.
# 4. else convert the difference into h:m format and print. 

def difference(h1, m1, h2, m2):
    # convert hour into minuts
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    
    if t1 == t2:
        print("Both are same time.")
        return
    else:
        diff = t2 - t1
        
    # Calculating hours from diff
    h = (int(diff/60)) % 24
    
    # Calculating minuts from diff
    m = diff % 60
    
    print(h, ":", m)
    
if __name__ == "__main__":
    difference(7, 20, 9, 45)
    difference(15, 23, 18, 54)
    difference(16, 20, 16, 20)
    
