
def prime_no(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print(n,"is Not a prime")
                break
        else: 
            print(n,"is a Prime no")
    else:
        print(n,"is not a Prime no")
        
prime_no(17)