#6. Python program to find the union of two lists.

li1 = [10,15,51,52,25]
li2 = [15,20,25,40,42]

union = list(set(li1) | set(li2))  #set ()remove duplicates no and | perform the union operation.


print('first list',li1)
print('second list',li2)
print('union of two lists',union)

