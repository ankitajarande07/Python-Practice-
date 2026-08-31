#3. WAP to input angles of a triangle and check whether triangle is valid or nat.

a = int(input('Enter 1st angle:'))
b = int(input('Enter 2nd angle:'))
c = int(input('Enter 3rd angle:'))

if a+b+c == 180:
    print('Triangle is valid:')
else:
    print('Triangle is nat valid:')
        