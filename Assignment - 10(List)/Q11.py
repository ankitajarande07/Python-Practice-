#11. Write a program to print all numbers which are divisible by m and n in the list.

li = [10,20,15,12,24,40,60]

m = int(input('enter the number m:'))
n = int(input('enter the number n:'))


for i in li:
    if i % m == 0 and i % n == 0:

     print('Number divisible by', m and n)
print(i)   