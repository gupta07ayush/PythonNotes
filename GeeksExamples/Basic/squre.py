def square(n):
    y = [x**2 for x in range(1,n+1)]
    return sum(y)
    
num = 12
print(f"Sum of squares of first {12} natural numbers is",square(num))