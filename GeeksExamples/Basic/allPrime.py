#Python Program to print all prime number in an interval

def allPrime(s, e):
    prime = []
    for i in range(s,e):
        if i==0 or i==1:
            continue
        else:
            for j in range(2, int(i/2+1)):
                if i % j == 0:
                    break
            else:
                prime.append(i)
    return prime
    
start, end = 10, 50
n = allPrime(start, end)

if len(n)==0:
    print("There are no prime number between this list exist.")
else:
    print("Prime numbers in this list are: \n",n)
