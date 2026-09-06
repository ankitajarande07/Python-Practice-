#4. WAP to print Armstrong number within a given range.

start = int(input('Enter starting number:'))
end = int(input('Enter ending number:'))

print('Armstrong Number:')
for num in range(start,end+1):
    temp = num
    count = 0

    while temp > 0:
        digit = temp % 10
        count = count + (digit ** 3)
        temp = temp // 10

    if count == num:
        print(num)  
