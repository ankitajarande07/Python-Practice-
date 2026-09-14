#4.  WAP to find sum of n number using recursive function...

def sum_num(num):
    if num == 0:
        return 0
    else:
        return num + sum_num(num-1)

num = int(input('Enter the number'))
result = sum_num(num)
print(result)    