#Roman Dattilo
#Professor Eckert
#CS-175L-01
#January 29th, 2023

    #Stocks Program

    #Variables

purchasePrice=float(input("At what value was your stock when you purchased? "))

purchaseCommission=float(input("What is the commission paid on your stock? "))

soldFor=float(input("What is the amount the stock sold for? "))

sellingCommission=float(input("What was the amount of commission on your sale? "))


#Profit equation

profit=soldFor-(purchasePrice+purchaseCommission+sellingCommission)



#final results

print('This is the value you purchased your stock at!: ', purchasePrice)
print('This is the commission that was paid on the purchase!: ', purchaseCommission)
print('You sold your stock for: ', soldFor)
print('The commission paid on sale: ', sellingCommission)
print('The profit(or loss if negative) is: ', profit)
