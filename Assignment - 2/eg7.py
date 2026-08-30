#7. Find the sum of three digit number.

num = int(input('Enter the three digit numbers:'))

first = num // 100
second = (num // 10) % 10
thrid = num % 10

sum = first + second + thrid 

print('sum of digits:', sum)