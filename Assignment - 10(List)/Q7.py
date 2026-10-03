#7. Write a program to create a new list from existing list which contains cube of each number of list.


li = [11, 22, 33, 44, 55]

cube =[]

for i in li:
    cube.append(i*i*i)

print('Cube list', cube)    