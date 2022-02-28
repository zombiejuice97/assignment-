
greatest = 0
def greatestn(numbers):
   #had to do this below because python takes great as a local 
   # variable and assigning it value inside the function is weird
   # you get a referenced before assignment error.

    great = greatest
    if(numbers[0]>numbers[1] and numbers[0]>numbers[2]):
         great = numbers[0]
    elif(numbers[1]>numbers[0] and numbers[1]>numbers[2]):
                great = numbers[1]
    else:
        great= numbers[2]
    return great

print(greatestn([2,8,9])) 