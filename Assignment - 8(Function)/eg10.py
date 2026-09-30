#10.Write a program to check if entered year is a leap year or not.

def check_leap_year(year):
    if(year % 400 == 0):                    # It is divisible by 400

     return 'leap year'
    else:
       return 'Not leap year'

year = int(input('Enter the year'))
result = check_leap_year(year)
print(result)    