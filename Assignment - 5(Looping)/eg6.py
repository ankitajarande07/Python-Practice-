#6. Write a program to print first n prime numbers.

num = int(input('Enter the number:'))

for num in range(2,num):
    count = 0

    for i in range(1,num+1):
     if num  % i == 0:
      count = count + 1

    if count == 2:
      print(num) 