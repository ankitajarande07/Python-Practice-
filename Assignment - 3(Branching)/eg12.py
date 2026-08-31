#12. Write a program to check if given 3 digit number is a palindrome or not.

# Plindrom number: It is a whose reverse is equal to the original number.
#  eg. 121,1331

num = int(input('Enter the number'))

original = num
reverse = 0

while (num > 0):
    digit = num % 10
    num = num // 10 
    reverse = reverse * 10 * digit
    

if (num == reverse):
    print('Palindrom number')
else:
    print('Not palindrom number')        
