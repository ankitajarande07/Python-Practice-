start = int(input('Enter the starting number of range:'))
end = int(input('Enter the ending number of range:'))

for num in range (start, end + 1):
    if num > 1:
        for i in range (2, num):
            if num % i == 0:
                break
        print(num)
