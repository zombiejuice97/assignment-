def factorial(number):
    fact = 1
    for elements in range(1,number+1):
        fact = fact * elements
    return fact

print(factorial(5)) 