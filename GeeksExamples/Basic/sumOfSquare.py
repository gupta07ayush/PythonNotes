# Python Program for Sum of squares of first n natural numbers.
# Given a positive integer N. The task is to find 1² + 2² + 3² + … + N²  
num = 5

def sum_square(n):
    s = [x*x for x in range(1,n+1)]
    print(sum(s))
print("Method 1 = ",end=" ")
sum_square(num)



# Method 2
s=0
def sum_square2(n):
    for i in range(1,n+1):
        global s 
        s = s + i*i
    print(s)
print("Method 2 = ",end=" ")
sum_square2(num)



# Method 3
def squaresum(n) :
    return (n * (n + 1) * (2 * n + 1)) // 6
print("Method 3 = ",end=" ")
print(squaresum(num))



# Method 3
def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
print("Method 4 = ",end=" ")
print(squaresum(num))