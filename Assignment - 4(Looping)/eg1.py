#1. WAP to print all even number until n.

num = int(input('Enter the even numbers'))

for i in range(1,num+1):
    if i % 2 == 0:
        print(i)