def gcd(num1,num2):
    #lists where the factors of the first and second number are stored
    lis1=[]
    lis2=[]
    #lists where the divisiors of the first and second number are stored 
    divisor1 =[]
    divisor2=[]
    common_factors =[]
    max=0
    #loops to find factors of a number 
    for i in range(1,num1+1):
        if(num1%i==0):
            lis1.append(i)
        
    for j in range(1,num2+1):
        if(num2%j==0):
            lis2.append(j)
    
    for k in lis1:
        if(num1%k==0):
            divisor1.append(k)
    
    for l in lis2:
        if(num2%l==0):
            divisor2.append(l)

    print(divisor1)
    print(divisor2)
    
    #Loop to find commonfactors
    for m in divisor1:
        for n in divisor2:
         if(m==n):
            common_factors.append(m)
    
    #loop to find the gcd
    for p in common_factors:
        if(p>max):
            max=p
    return max


print(gcd(6,8))




