#6.  WAP to print fibonacci series using recursion....

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num = int(input('Enter the number'))
print('fibonacci series')  


for i in range(num):
    print(fibonacci(i), end =" ")

    