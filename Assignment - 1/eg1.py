#1. Write a program to calculate the percentage of student based on marks of any subjects.

#Take input marks of subjects
m1 = int(input('Enter the marks of subject 1:'))
m2 = int(input('Enter the marks of subject 2:'))
m3 = int(input('Enter the marks of subject 3:'))
m4 = int(input('Enter the marks of subject 4:'))
m5 = int(input('Enter the marks of subject 5:'))

#Perform operation
total = m1 + m2 + m3 + m3 + m5
#calculate the percentage
percentage = total / 5

#display resuit
print('Total=',total)
print('Percentage=',percentage)
