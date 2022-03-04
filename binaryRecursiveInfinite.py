def binSearchRec(numbers,high,key):
    low = 0
    while(low<=high):
        mid = (low+high)//2 
        if(key==numbers[mid]):
            return numbers[mid]
        elif(key<numbers[mid]):
            binSearchRec(numbers,mid-1,key)
        elif(key>numbers[mid]):
            low = mid+1
        else:
            return 0

print(binSearchRec([1,20,30,40,50,60,70,80,90,100],10,80))