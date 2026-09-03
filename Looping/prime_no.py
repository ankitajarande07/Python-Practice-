num = int(input('Enter the number'))
count = 0
for i in range(2, num):
    if num % i == 0:
       count = 1

if count == 0:
    print('The number is prime')
else:
    print('The number is not prime')
