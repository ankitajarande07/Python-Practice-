num = int(input('Enter the number:'))
sumDivisar = 0
for i in range (1, num):
    if num % i == 0:
        sumDivisar = sumDivisar + i
        # sumDivisar+=i
if sumDivisar == num:
    print('number is perfect:')
else:
    print('number is not perfect:')
                