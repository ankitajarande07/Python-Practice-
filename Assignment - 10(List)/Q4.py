#4.  Write a program to reverse the list. 

li = [10, 20, 30, 40, 50]

reverse = []

i = len(li)-1
while i >= 0:
    reverse.append(li[i])
    i -= 1

print('Reverse list', reverse)