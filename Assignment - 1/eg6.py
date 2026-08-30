#6. Write a program to input two angles from user and find third angle of the triangle.

 # Take input of angle
a = float(input('enter angle1:'))
b = float(input('enter angle2:'))

# Perform OPeration
Triangle = 180 - (a + b)

print('Third angle =',Triangle)
