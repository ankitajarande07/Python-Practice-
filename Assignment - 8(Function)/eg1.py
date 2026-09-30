#1. Write a program to calculate area of rectangle...    # Type2

def area_rectangle(lingth, breadth):
    area = lingth * breadth
    return area 

a = float(input('Enter the length:'))
b = float(input('Enter the breadth:'))

result = area_rectangle(a,b)

print(result)