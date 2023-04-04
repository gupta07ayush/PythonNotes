num = 153
#print(ord)


def arm(n):
    ord = len(str((num)))
    n = str(n)
    
    print(n,"is given number and",end=" ")
    a = 0   
    for i in (n):
        a += int(i)**ord    
    if a == num:
        print(num, "is a armstrong Number")
    else:
        print(num, "IS NOT A ARMSTRONG NO")
        
arm(num)




"""
The Armstrong numbers of first kind  are 
1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817.
"""