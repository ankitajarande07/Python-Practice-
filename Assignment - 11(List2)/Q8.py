#8. Print 1 to 100 in snakes and ladder pattern.

n = 1

for row in range(10):
    numbers = []

    for col in range(10):
        numbers.append(n)
        n = n+1

    if row %2!=0:
        numbers.reverse()

    print(numbers)    
