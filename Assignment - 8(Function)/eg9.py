#9. Write a program to check if entered number is a palindrome or not.

def pallindrome(num):
    temp = num
    rev = 0

    while (temp>0):
        digit = temp % 10
        temp = temp // 10
        rev = rev * 10 + digit

    if (num == rev):
        return True
    else:
        return False

num = int(input('Enter the number:'))
#result = pallindrome(num)
#print(result)

if pallindrome(num):
    print('Pallindrome number')
else:
    print('Not pallindrome number')

       


