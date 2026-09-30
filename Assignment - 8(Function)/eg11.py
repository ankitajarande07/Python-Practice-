#11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def isArmstrong(num):
    temp = num 
    sum = 0
    while(temp > 0):
        d = temp % 10
        print('digit:',d)
        temp = temp // 10

        sum = sum + (d*d*d)
        print('sum:',sum)

    if(num == sum):
        return True
    else:
        return False

num = int(input("Enter the number"))
res = isArmstrong(num)
print(res)             