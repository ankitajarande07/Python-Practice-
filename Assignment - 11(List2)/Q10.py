#10. write a program to print list after removing even number

li = [18,32,43,85,16,46,65]

for i in li[:]:       # li[:] creates a copy of the list, we can safly remove element for list 
    if i%2==0:
        li.remove(i)

print('remove even number',li)
