#6. WAP to calculate profit or loss.

# Profit = selling price - cost price
# loss = cost price - selling price
# no profit no loss 

cp = int(input('Enter the cp:'))
sp = int(input('Enter the sp:'))

if(sp < cp):
    profit = sp - cp
    print("Profit")
elif(cp > sp):
    loss = cp - sp
    print("loss") 
else:
    print("No profit no loss")       