#4. Python Program to Find the Second Largest Number in a List Using Bubble Sort.

li = [60,50,40,65,98,85]
n = len(li)
for i in range(1, n):
    for j in range(0, n-1):
        if(li[j] > li[j + 1]):
            li[j], li[j + 1] = li[j + 1], li[j]

print('bubble sort',li)
            

