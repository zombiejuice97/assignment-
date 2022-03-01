def avgasPercentage(numbers):
    sum = 0
    for number in numbers[:3]:
        sum = sum + number 
    average = sum/3
    percentage = average/numbers[3]
    return percentage

print(avgasPercentage([1,2,6,10]))



