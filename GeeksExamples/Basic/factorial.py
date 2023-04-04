#Python Program for factorial of a number



#recursion
def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n-1)
print(fact(5))

#while loop
def fact2(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact = fact * n
            n=n-1
        return fact
print(fact(5))



#for loop
def fact3(n):
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    return fact
print(fact(5))
