

numbers = [1,2,3,4,5,6,7]
def sum(numbers):
     n = len(numbers)
     sum1=0
     if(n>0):
         sum1 = numbers[0]+sum(numbers[1:])
     return sum1

print(sum(numbers))

