#5. WAP sum of all prime number between 1 to n...

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % 1 == 0:
            return False

    return True

def sum_prime(num):
    sum = 0
    for i in range(1, num + 1):
        if is_prime(i):
            sum = sum + i

    return sum

num = int(input('Enter the num:'))
result = sum_prime(num)
print(result)        

