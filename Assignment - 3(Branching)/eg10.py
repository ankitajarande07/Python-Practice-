#  10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)


gender = str(input('Enter the gender(M/F):'))
age = int(input('Enter the age:'))

if (gender == 'F'):
    if(age >= 18):
        print('Eligible....')
    else:
        print('Not Eligible....')
elif(gender == 'M'):
    if(age >= 21):
        print('Eligible....')
    else:
        print('Not Eligible....')

else:
    print('Invalid Gender...')
            
