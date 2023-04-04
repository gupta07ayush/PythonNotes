# Method 1
p,r,t = (input("Enter Principal,rate, and time: ")).split()
print(p,r,t)

si = (int(p)*int(r)*int(t))/100
print(si,"%")


# Method 2
def si(p,r,t):
    si = (p*r*t)/100    
    print("Simple interest is ",si)
si(100,10,2)


# Compount interest
#a = p(1+r/100)**t
#CI = a-p

def ci(p,r,t):
    ci = (p*(1+r/100)**t) - p
    print(ci)
    
ci(100,5,2)
    