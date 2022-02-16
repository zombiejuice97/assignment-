def factors(num):
    facs = []
    for i in range(1,num+1):
        facs.append(i)
    return facs

def Divisor(factors,y):
    divisors =[]
    x = factors(y)
    for i in x:
        
        if(y%i==0):
            divisors.append(i)
        
    return divisors 


print(Divisor(factors,6))
print(Divisor(factors,8))

