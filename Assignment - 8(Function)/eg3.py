#3.  Write a program to find sum of following series using functions :
#    a. 1+ 2 + 3 + 4+..... + n
#    b. 1!+ 2! + 3! + 4!+..... + n!
#    c. 1^1 + 2^2 + 3^3+ ...... n^n

#(a) .....
def sum_series(num):
    sum = 0

    for i in range(1, num+1):
        sum = sum + i

    return sum

num = int(input('Entre num:'))
result = sum_series(num)
print(result)    

#(b).....
def factorial(num):
    fact = 1
    for  i in range(1, num +1):
        fact = fact * i
    return fact

def sum_factorial_series(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + factorial(i)
    return sum

num = int(input('Enter the num:'))
result = sum_factorial_series(num)
print(result)


#(c).....

def sum_power_series(num):
    sum = 0
    
    for i in range(1, num+1):
        sum = sum + i ** i

    return sum

num = int(input('Enter num:'))
result = sum_power_series(num)
print(result)    
 