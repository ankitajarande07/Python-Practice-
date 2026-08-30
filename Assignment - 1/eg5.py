#5. Write a program to enter P, R, T and calculate compound interest.

# Take input of amount
p = int(input('Enter principal:'))
r = int(input('Enter Rate:'))
t = int(input('Enter time:'))

# Perform Operation
CI = p(1 + r / 100)*t - p


# Display result
print('Compound Interest =',CI)
