num = int(input('Enter the number:'))

temp = num

while(temp > 0):
    d = temp % 10
    temp = temp // 10
    print(d)