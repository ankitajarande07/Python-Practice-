#4. Sum of all odd numbers between 1 to n

def sum_odd(num):
    sum = 0

    for i in range(1, num+1, 2):
        sum = sum + i
    return sum 

num = int(input('Enter the num:'))
result = sum_odd(num)
print(result)    