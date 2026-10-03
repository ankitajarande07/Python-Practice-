#10. Write a program to remove all occurrences of a given element in the list.

li = [10,20,25,35,65,45]

li = []

for i in li:
    if i!=i:
        li.append(i)

print('Remove the element',li)
