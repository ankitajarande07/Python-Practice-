#2.  Write a program to check if given number is Armstrong or not using recursive function.

def count_digits(num):
    if num == 0:
        return 0
    else:
        return 1 + count_digits(num // 10)

def armstrong(num, digits, original):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return digit ** digits + armstrong(num // 10, digit, original) 

num = int(input('Enter the number'))
digits = count_digits(num)
sum_value = armstrong(num, digits, num)

if sum_value == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")
    