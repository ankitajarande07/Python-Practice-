#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = int(input('Enter the marks of subject 1:'))
m2 = int(input('Enter the marks of subject 2:'))
m3 = int(input('Enter the marks of subject 3:'))
m4 = int(input('Enter the marks of subject 4:'))
m5 = int(input('Enter the marks of subject 5:'))

Total = m1 + m2 + m3 + m4 + m5
parcentage = Total / 5

print('Total marks', Total)
print('parcentage', parcentage)

if parcentage >= 70:
    print('Grade: First class')
elif parcentage >= 85:
    print('Grade: Second class')
elif parcentage >= 69:
    print('Grade: Thrid class')
elif parcentage >= 90:
    print('Grade: Pass class') 
else:
    print('Grade: Fa ne                                                                  1il class')               