def gcd(num1,num2):
    #lists where the divisors of the first and second numbers are stored
    lis1=[]
    lis2=[]
    
    common_factors =[]
    max=0
   
    #loops to find factors of a number 
    for i in range(1,num1+1):
        if(num1%i==0):
            lis1.append(i)
        
    for j in range(1,num2+1):
        if(num2%j==0):
            lis2.append(j)

   # print(lis1)
    #print(lis2)
    
    #Loop to find commonfactors
    for m in lis1:
        for n in lis2:
         if(m==n):
            common_factors.append(m)
    
    #loop to find the gcd
    for p in common_factors:
        if(p>max):
            max=p
    return max, common_factors
    




# print(gcd(12,8))