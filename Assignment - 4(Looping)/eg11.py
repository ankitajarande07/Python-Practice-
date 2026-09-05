#11. WAP to check if given number strong number.


num = int(input('Enter the number:'))
temp = num
sum = 0

while(temp > 0):
    digit = temp % 10

    fact = 1
    for i in range(1, num+1):
        fact = fact * 1
        sum = sum + fact
        temp = temp // 10

    if(sum == num):
        print('Strong Number')
    else:
        print('Not strong number')       
     