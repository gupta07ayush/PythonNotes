#Python Program for n-th Fibonacci number

def fibo(n):
    if n<=0:
        print("invalid input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        

num = 10
print(fibo(num))