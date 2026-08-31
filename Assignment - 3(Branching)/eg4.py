#4. WAP to input all sides of a triangle and check whether triangle is valid or not.

a = int(input('Enter 1st sides:'))
b = int(input('Enter 2nd sides:'))
c = int(input('Enter 3rd sides:'))

if (a+b>c) and (a+c>b) and (b+c>a):
    print('Triangle is valid:')
else:
    print('Triangle is not valid:')
        