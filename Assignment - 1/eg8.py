#8. Write a program to convert days into years, weeks and days.

# Take input form user
days = int(input('Enter days:'))

# Perform Operation 
years = days // 365
days = days % 365

weeks = days // 7
days = days % 7

print('Years =', years)
print('Weeks =',weeks)
print('Days =',days)
