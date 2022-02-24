def lcm(number1,number2):
   #variables to store the multiples of the numbers
   multiple1=[] 
   multiple2=[]
   #list to store the common multiples 
   common=[]
   
   #loops to collect multiples of numbers 
   for numberx in range(1,10):
       num1=number1*numberx
       multiple1.append(num1)

   for numbery in range(1,10):
        num2=number2*numbery
        multiple2.append(num2)    
    
    #to find the common multiples 
   for m in multiple1:
        for n in multiple2:
            if(m==n):
                common.append(m)
   # to find the least of the common multiples 
   min=common[0]
   for elements in common:
        if(len(common)==1):
            min = elements
        elif(elements<min):
            min = elements
   return min

print(lcm(30,60))
