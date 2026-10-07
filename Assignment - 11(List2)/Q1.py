#1. Python Program to Put Even and Odd elements of a List into two Different lists.

li = [15,25,32,14,20,45,30]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)            