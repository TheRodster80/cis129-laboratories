# Author: Jarrod Saffioti
# CIS129 Lab 3
# This is an interactive coffee shop

COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TAX_PERCENT = 6

print('***************************************\nMy Coffee and Muffin Shop')

#Input from user
numCoffee = float(input('Number of coffees bought? '))
numMuffin = float(input('Number of muffins bought? '))

#Calculation of all costs
costCoffee = numCoffee * COFFEE_PRICE 
costMuffin = numMuffin * MUFFIN_PRICE

totalBeforeTax = costCoffee + costMuffin
tax = totalBeforeTax * TAX_PERCENT/100
totalAfterTax = tax + totalBeforeTax

#Receipt output
print('***************************************\n\n***************************************\nMy Coffee and Muffin Shop Receipt\n')
print(str(int(numCoffee)) + ' Coffees at $5 each: $' + str(costCoffee) + '\n' + str(int(numMuffin)) + ' Muffins at $4 each: $' + str(costMuffin))
print('6% tax: $' + str(tax) + '\n---------\nTotal: $' + str(totalAfterTax) + '\n***************************************')
