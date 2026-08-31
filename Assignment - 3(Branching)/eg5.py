#5. WAP to check whether the triangle is equilateral, isosceles or scalene triangle

a = int(input('Enter 1st sides:'))
b = int(input('Enter 2nd sides:'))
c = int(input('Enter 3rd sides:'))

if a == b and b == c:
    print('Equilateral triangle')
elif a == b / b == c / a == c:
    print('Isosceles Triangle')
else:
    print('scalene Triangle')        