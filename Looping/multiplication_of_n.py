#WAP to print multiplication table of n (Take n from user).

n = int(input('Enter the value of n:'))
for i in range(n, n * 10 + 1, n):
    print(i)