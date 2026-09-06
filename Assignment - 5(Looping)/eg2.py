#2. Enter number of students from user. For those many students accept marks of 5
#   subject marks from user and calculate percentage. Display all percentage and
#   average percentage of students.


num = int(input('Enter number of students:'))

total_percentage = 0

for i in range(1,num+1):
    print('Number of student',i)
    total_marks = 0

    for j in range(1,6):
        marks = float(input('Enter marks of subject:'))
        total_marks += marks

    percentage = total_marks / 5
    total_percentage += percentage     

    print('Percentage of student', i)

average = total_percentage / num

print('average Percentage:', average)