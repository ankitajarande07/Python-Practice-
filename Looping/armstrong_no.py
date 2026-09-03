num = int(input('Enter the number:'))
temp = num
count = 0
while temp > 0:
    d = temp % 10
    count = count + (d**3)
    temp =  temp // 10
if count == num:
    print('Armstrong number')
else:
    print('Not armstrong number')
            