#4. Write a program to enter P, T, R and calculate simple interest.

# Take input of amount
p = int(input('Enter principal:'))
r = int(input('Enter rate:'))
t = int(input('Enter time:'))

# perfor Operation
SI = (p*r*t)/100

# Display result
print('Simple Interest =',SI)
