#7.  WAP to find the sum of digits using recursion ...

def sum_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_digits(num // 10)


num = int(input('Enter the number'))
result = sum_digits(num)
print(result)
    