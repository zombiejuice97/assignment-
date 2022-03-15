# arr = [10,16,8,12,15,6,3,9,5]
def partition(i,j,arr):
    if(i==j):
        return
    pivot = arr[0]
   # i=1
    # j=len(arr)-1
    while(i<=j):
        if(arr[i]>pivot):
            if(arr[j]<pivot):
                x=arr[j]
                arr[j]=arr[i]
                arr[i]=x
                j-=1
                print('i is ' + str(arr[i]))
                print('j is ' + str(arr[j]))
            else:
                j-=1
        i+=1
        if(i>j):
             x = arr[j]
             arr[j] = arr[0]
             arr[0] = x
            
   # partition(1,len(numbers)-1,arr)
    return j

digits =  [10,16,8,12,15,6,3,9,5]

# print(partition(1,len(numbers)-1,numbers))

def quicksort(low,high):
    if(low>high):
        return
    else:
        j = partition(low,high,digits)
        quicksort(low,j-1)
        quicksort(j+1,high)
    

print(quicksort(1,len(digits)-1))