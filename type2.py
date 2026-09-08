# Function type 2: With passing parameter without returning value

def addition(num1, num2):
    sum = num1 + num2

    print(f'Addition is {sum}.')

x = int(input('Enter number 1:'))
y = int(input('Enter number 2:'))

addition(x, y)