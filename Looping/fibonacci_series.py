n = int(input('How many fibonacci number you want:'))

a = -1
b = 1

for i in range (n):    #0,1,2,3,4,5,6,7,8,9 
    c = a + b
    print(c)
    a = b
    b = c