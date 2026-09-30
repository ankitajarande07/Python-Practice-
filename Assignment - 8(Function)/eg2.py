#2.  Write a program to calculate area of circle....#Type3

def area_circle(radius):
    area = 3.14 * radius * radius
    return area 

radius = float(input('Enter the radius'))
result = area_circle(radius)
print(result)  
