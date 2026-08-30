#5. WAP to calculate selling price of book based on cost price and discount.

cp = int(input('Enter the cost price:'))
discount = int(input('Enter the discount:'))

sp = cp - (cp * discount / 100)

print('selling price:', sp)