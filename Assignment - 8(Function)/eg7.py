#7. Write a program to find sum of digits of a number. 

def sumofdigits(n):
    total = 0

    while n>0:
        digit = n % 10 
        n = n // 10
        total = total + digit 
    return total    

n = int(input('Enter the number:'))
result = sumofdigits(n)
print(result)


