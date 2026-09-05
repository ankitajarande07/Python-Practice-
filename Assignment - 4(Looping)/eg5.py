#5. WAP to print fibonacci series upto n...

num = int(input('Enter the number'))
a = -1
b = 1

for i in range(num):     # 0,1,2,3,4,5,6,7,8,9
    c = a+b
    print(c)
    a = b
    b = c
