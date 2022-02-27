
def com(principle,rate,months,years):
    amount = principle*((1+(rate/months))**(months*years))
    print(amount)

com(100,0.07,12,4)




