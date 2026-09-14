#10.  WAP to reverse a number using recursion...

def reverse(num,rev=0):
    if num == 0:
        return rev
    else:
        return reverse(num // 10, rev * 10 + num % 10)

num = int(input('Enter the number'))
result = reverse(num)
print(result)    