#5. WAP to find the factorial using recursion...

def factorial(num):
    if (num == 1):
        return 1
    else:
        return num * factorial(num - 1)

num = int(input('Enter the number'))
result = factorial(num)
print(result)      
