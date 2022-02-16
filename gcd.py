
class gcd:
    
      
    def __init__(self,num,num2):
        self.num = number1
        self.num2 = number2
    facs = []
    facs2=[]
    for i in range(1,number1+1):
        facs.append(i)
    
    for j in range(1,number2+1):
        facs2.append(j)

    divisors =[]
    divisors2 =[]
  

    for k in facs:
        if(number1%k==0):
            divisors.append(i)
    
    for l in facs2:
        if(number2%l==0):
            divisors2.append(l)

    print (divisors,divisors2)


example2 = gcd(6,8)
