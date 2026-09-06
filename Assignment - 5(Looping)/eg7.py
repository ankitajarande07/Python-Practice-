#7. Write a program to solve the following series :
#   a. 1! + 2! + 3! + 4! + .....n!

num = int(input('Enter the number:'))
fact = 1
sum = 0

for i in range(1,num+1):
    fact = fact * 1
    sum = sum + i

print('Sum:',sum)    


#   b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

num = int(input('Enter the N:'))
sum = 0

for i in range(1,num+1):
    sum = sum + num ** 1

print('sum',sum)    



#   c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

num = int(input('Enter the term:'))
term = 1
sum = 0

for i in range(1,num+1):
    sum = sum + term
    term = term * 2

print('sum',sum)    



#   d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = int(input('Enter a :'))

sum = 0

for i in range(1,11):
    sum = sum + ( a ** i)

print('sum',sum)    





#   e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input('Enter the x:'))
num = int(input('Enter the number of term:'))

sum = 0

for i in range(1, num + 1):
    term = (x ** i) / (2 * i - 1)

    if i % 2 == 1:
        sum = sum + term
    else:
        sum = sum - term

print("sum", sum)