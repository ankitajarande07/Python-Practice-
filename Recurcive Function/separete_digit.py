def separete_digit(num):
    if (num > 0):
        d = num % 10
        print(d)
        separete_digit(num//10)   

separete_digit(12345)



