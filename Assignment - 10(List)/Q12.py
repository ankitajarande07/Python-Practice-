#12. Write a program to create three lists of numbers, their squares and cubes

li = [1,2,3,4,5,6,7]

squares = []
cubes = []

for i in li:
    squares.append(i*i)
    cubes.append(i*i*i)

print('Squares', squares)
print('Cubes', cubes)    