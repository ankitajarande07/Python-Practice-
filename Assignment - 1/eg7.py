#7. Program to find the roots of a Quadratic Equation.

# Take input from user 
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('enter c:'))

# Perform operation 
d = b ** 2 - (4 * a * c)

r1 = (- b + (d ** 0.5)) / (2 * a)

r2 = (- b - (d ** 0.5)) / (2 * a)

print('Root 1;', r1)
print('Root 2:', r2)

