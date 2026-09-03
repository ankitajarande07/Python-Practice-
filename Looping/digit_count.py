num = int(input('Enter the number:'))
temp = num
count = 0
while(temp >0):
    d = temp % 10
    temp = temp // 10
    count += 1       # count = count + 1
print('Total count:', count)
    
