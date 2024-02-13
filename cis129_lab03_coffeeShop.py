# Author: Jarrod Saffioti
# CIS129 Lab 3
# This is an interactive coffee and muffin and cookie and water shop

COFFEE_PRICE = 5
MUFFIN_PRICE = 4
COOKIE_PRICE = 3
WATER_PRICE = 2
TAX_PERCENT = 6

print('***************************************\nMy Coffee and Muffin and Cookie and Water Shop')

#Input from user
numCoffee = float(input('Number of coffees bought? '))
numMuffin = float(input('Number of muffins bought? '))
numCookie = float(input('Number of cookies bought? '))
numWater = float(input('Number of waters bought? '))

#Calculation of all costs
costCoffee = numCoffee * COFFEE_PRICE
costMuffin = numMuffin * MUFFIN_PRICE
costCookie = numCookie * COOKIE_PRICE
costWater = numWater * WATER_PRICE

totalBeforeTax = costCoffee + costMuffin + costCookie + costWater
tax = totalBeforeTax * TAX_PERCENT/100
totalAfterTax = tax + totalBeforeTax

#Receipt output
print('***************************************\n\n***************************************\nMy Coffee and Muffin and Cookie and Water Shop Receipt\n')
print(str(int(numCoffee)) + ' Coffees at $5 each: $' + str(costCoffee) + '\n' + str(int(numMuffin)) + ' Muffins at $4 each: $' + str(costMuffin))
print(str(int(numCookie)) + ' Cookies at $3 each: $' + str(costCookie) + '\n' + str(int(numWater)) + ' Waters at $2 each: $' + str(costWater))

print('6% tax: $' + str(tax) + '\n---------\nTotal: $' + str(totalAfterTax) + '\n***************************************')
print('\nThanks for playing, User.')
